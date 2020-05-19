<template>
    <div>
        <!--        注册控件-->
        <wired-input id="emailInput" :value="email" @input="email=$event.target.value" placeholder="请输入邮箱"/>
        <wired-input id="userNameInput" :value="userName" @input="userName=$event.target.value" placeholder="请输入昵称"/>
        <wired-input type="password" id="pswInput" :value="psw" @input="psw=$event.target.value" placeholder="请输入密码"/>
        <wired-button id="registerBtn" v-on:click="register">注册</wired-button>
        <!--        注册控件-->
    </div>
</template>

<script>
    import CreateUser from '../../../graphql/user/CreateUser.graphql'
    export default {
        name: "SignUp",
        data() {
            return {
                email: '',
                userName: '',
                psw: ''
            }
        },
        methods: {
            register() {
                console.log(this.email, this.userName, this.psw)
                this.$apollo
                    .mutate({
                        mutation: CreateUser,
                        variables: {
                            email: this.email,
                            name: this.userName,
                            password: this.psw
                        }
                    })
                    .then(result => {
                        if (result.data.createUser.success) {
                            alert('注册成功')
                        } else {
                            alert('注册失败')
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
    #emailInput {
        position: absolute;
        margin-left: 430px;
        margin-top: 25%;
        width: 30%;
    }

    #userNameInput {
        position: absolute;
        margin-left: 430px;
        margin-top: 32%;
        width: 30%;
    }

    #pswInput {
        position: absolute;
        margin-top: 140px;
        margin-left: 10px;
        width: 30%;
    }

    #registerBtn {
        position: absolute;
        margin-top: 200px;
        margin-left: 12%;
    }
</style>