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
    </div>
</template>

<script>
    import ShowUser from '../../graphql/user/User.graphql'
    import RefreshToken from '../../graphql/user/RefreshToken.graphql'
    import UpdateUser from '../../graphql/user/UpdateUser.graphql'

    export default {
        name: "UserSet",
        data() {
            return {
                alteredName: '',
                alteredPsw: ''
            }
        },
        methods: {
            updateToken() {
                const refreshToken = localStorage.getItem('refreshToken');
                this.$apollo
                    .mutate({
                        mutation: RefreshToken,
                        variables: {
                            refreshToken: refreshToken
                        }
                    })
                    .then(result => {
                        // 把刷新的 token 等信息重新存储，覆盖旧信息
                        localStorage.setItem('exp', result.data.refreshToken.payload.exp);
                        localStorage.setItem('email', result.data.refreshToken.payload.email);
                        localStorage.setItem('origIat', result.data.refreshToken.payload.origIat);
                        localStorage.setItem('token', result.data.refreshToken.token);
                        localStorage.setItem('refreshToken', result.data.refreshToken.refreshToken);
                        localStorage.setItem('refreshExpiresIn', result.data.refreshToken.refreshExpiresIn);
                        console.log('更新后的exp:', result.data.refreshToken.payload.exp)
                    })
                    .catch((error) => {
                        console.log(error.message())
                    })
            },
            getCurrentTime() {
                let currentTime = ((new Date()).valueOf()) / 1000;
                console.log('currentTime:', currentTime)
                return currentTime
            },
            getToken() {
                const exp = localStorage.getItem('exp');
                const refreshExpiresIn = localStorage.getItem('refreshExpiresIn');
                console.log('exp - 30:', exp - 30)
                console.log('refreshExpiresIn - 60', refreshExpiresIn - 60)
                // payload 为空说明用户已经退出登录
                if (exp === '') {
                    alert('您尚未登录，请先登录！')
                    this.$router.push({path: '/signIn'})
                } else if (this.getCurrentTime() < (exp - 30)) {
                    // 当前时间戳小于 token 过期时间戳，说明 token 没过期
                } else if (this.getCurrentTime() < (refreshExpiresIn - 60)) {
                    // 当前时间戳大于等于 token 过期时间戳，但小于 refreshToken 时间戳
                    // 说明 token 过期，但是 refreshToken 没过期
                    this.updateToken();
                } else {
                    // refreshToken 和 token 都过期了
                    alert('登录信息已过期，请先登录！')
                    this.$router.push({path: '/signIn'})
                }
            },
            showInfo() {
                this.getToken();
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
                        if(result.data.user.weeklyReport){
                            document.getElementById("showReport").innerHTML = "Report weekly";
                        }else if (result.data.user.monthlyReport) {
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
</style>