<template>
    <div>
        <!--        查询个人信息控件-->
        <wired-button id="showInfoBtn" v-on:click="showInfo">查询个人信息</wired-button>
        <div id="userInfoList">
            <wired-card id="showEmail"></wired-card>
            <wired-card id="showName"></wired-card>
            <wired-card id="showPsw"></wired-card>
            <wired-card id="showRemind"></wired-card>
            <wired-card id="showReport"></wired-card>
        </div>
        <!--        查询个人信息控件-->

        <!--        更改个人信息控件-->
        <wired-input id="alterNameInput" :value="alteredName" @input="alteredName=$event.target.value"
                     placeholder="请输入修改后的昵称"/>
        <wired-input type="password" id="alterPswInput" :value="alteredPsw" @input="alteredPsw=$event.target.value"
                     placeholder="请输入修改后的密码"/>
        <wired-button id="alterInfoBtn" v-on:click="alterInfo">保存更改</wired-button>

        <!--        更改个人信息控件-->

        <!--        注销用户控件-->
        <wired-button id="deleteBtn" v-on:click="del">注销用户</wired-button>
        <!--        注销用户控件-->
    </div>
</template>

<script>
    import ShowUser from '../../graphql/user/User.graphql'
    import UpdateUser from '../../graphql/user/UpdateUser.graphql'
    import {getToken} from '../../getToken'
    import DeleteUser from '../../graphql/user/DeleteUser.graphql'


    export default {
        name: "UserSet",
        data() {
            return {
                alteredName: '',
                alteredPsw: ''
            }
        },
        methods: {
            async showInfo() {
                if (!await getToken()) {
                    return
                }
                this.$apollo
                    .mutate({
                        mutation: ShowUser
                    })
                    .then(result => {
                        document.getElementById("showEmail").innerHTML = result.data.user.email;
                        document.getElementById("showName").innerHTML = result.data.user.name;
                        document.getElementById("showPsw").innerHTML = result.data.user.password;
                        if (result.data.user.dailyRemind) {
                            document.getElementById("showRemind").innerHTML = "Remind daily";
                        } else if (result.data.user.weeklyRemind) {
                            document.getElementById("showRemind").innerHTML = "Remind weekly";
                        } else if (result.data.user.monthlyRemind) {
                            document.getElementById("showRemind").innerHTML = "Remind monthly";
                        } else if (result.data.user.yearlyRemind) {
                            document.getElementById("showRemind").innerHTML = "Remind yearly";
                        }
                        if (result.data.user.weeklyReport) {
                            document.getElementById("showReport").innerHTML = "Report weekly";
                        } else if (result.data.user.monthlyReport) {
                            document.getElementById("showReport").innerHTML = "Report monthly";
                        } else if (result.data.user.yearlyReport) {
                            document.getElementById("showReport").innerHTML = "Report yearly";
                        }
                        alert('已将个人信息全部显示')
                    })
                    .catch((error) => {
                        console.log(error.message)
                    })
            },
            alterInfo() {
                this.$apollo
                    .mutate({
                        mutation: UpdateUser,
                        variables: {
                            name: this.alteredName,
                            password: this.alteredPsw
                        }
                    })
                    .then((result) => {
                        if (result.data.updateUser.success) {
                            alert('修改成功')
                        } else {
                            alert('修改失败')
                        }
                    })
                    .catch((error) => {
                        console.log(error.message)
                    })
            },
            async del() {
                if (!await getToken()) {
                    return
                }
                this.$apollo
                    .mutate({
                        mutation: DeleteUser
                    })
                    .then((result) => {
                        if (result.data.deleteUser.success) {
                            alert('注销成功')
                        } else {
                            alert('注销失败');
                        }
                    })
                    .catch((error) => {
                        console.log(error.message)
                    })
            }
        }
    }
</script>

<style scoped>
    #showInfoBtn {
        position: absolute;
        margin-top: 10px;
        margin-left: 20px;
    }

    #userInfoList {
        position: absolute;
        margin-top: 70px;
        margin-left: 20px;
        width: 100%;
        height: 100%;
    }

    #alterNameInput {
        position: absolute;
        margin-top: 200px;
        margin-left: 20px;
        width: 350px;
    }

    #alterPswInput {
        position: absolute;
        margin-top: 270px;
        margin-left: 20px;
        width: 350px;
    }

    #alterInfoBtn {
        position: absolute;
        margin-top: 340px;
        margin-left: 130px;
    }

    #deleteBtn {
        position: absolute;
        margin-left: 590px;
        margin-top: 190px;
    }
</style>