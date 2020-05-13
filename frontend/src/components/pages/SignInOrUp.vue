<template>
    <div>
        <!--        注册控件-->
        <wired-input id="emailInput" :value="email" @input="email=$event.target.value" placeholder="请输入邮箱"/>
        <wired-input id="userNameInput" :value="userName" @input="userName=$event.target.value" placeholder="请输入昵称"/>
        <wired-input type="password" id="pswInput" :value="psw" @input="psw=$event.target.value" placeholder="请输入密码"/>
        <wired-button id="registerBtn" v-on:click="register">注册</wired-button>
        <!--        注册控件-->

        <!--        登录控件-->
        <wired-input id="emailInputLogin" :value="emailLogin" @input="emailLogin=$event.target.value"
                     placeholder="请输入登录邮箱"/>
        <wired-input type="password" id="pswInputLogin" :value="pswLogin" @input="pswLogin=$event.target.value"
                     placeholder="请输入登录密码"/>
        <wired-button id="loginBtn" v-on:click="login">登录</wired-button>
        <!--        登录控件-->

        <!--        注销用户控件-->
        <wired-button id="deleteBtn" v-on:click="del">注销用户</wired-button>
        <!--        注销用户控件-->

        <!--        退出登录控件-->
        <wired-button id="logoutBtn" v-on:click="logout">退出登录</wired-button>
        <!--        退出登录控件-->
    </div>
</template>

<script>
    import CreateUser from '../../graphql/user/CreateUser.graphql'
    import Login from '../../graphql/user/Login.graphql'
    import DeleteUser from '../../graphql/user/DeleteUser.graphql'
    import Logout from '../../graphql/user/Logout.graphql'

    export default {
        name: "SignInOrUp",
        data() {
            return {
                email: '',
                userName: '',
                psw: '',
                emailLogin: '',
                pswLogin: ''
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
            },
            login() {
                this.$apollo
                    .mutate({
                        mutation: Login,
                        variables: {
                            email: this.emailLogin,
                            password: this.pswLogin
                        },
                    })
                    .then(result => {
                        localStorage.setItem('exp', result.data.tokenAuth.payload.exp);
                        localStorage.setItem('email', result.data.tokenAuth.payload.email);
                        localStorage.setItem('origIat', result.data.tokenAuth.payload.origIat);
                        localStorage.setItem('token', result.data.tokenAuth.token);
                        localStorage.setItem('refreshToken', result.data.tokenAuth.refreshToken);
                        localStorage.setItem('refreshExpiresIn', result.data.tokenAuth.refreshExpiresIn);
                        console.log('登录获取到的payload:', JSON.stringify(result.data.tokenAuth.payload));
                        console.log('登录获取到的token:', result.data.tokenAuth.token);
                        console.log('登录获取到的refreshToken:', result.data.tokenAuth.refreshToken);
                        console.log('登录获取到的refreshExpiresIn:', result.data.tokenAuth.refreshExpiresIn);
                        alert('登录成功，token & refreshToken 已保存。');
                        this.$router.go(-1);
                    })
                    .catch((error) => {
                        alert('登录失败。');
                        console.log(error.message);
                    });
            },
            del() {
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
            },
            logout() {
                const refreshToken = localStorage.getItem('refreshToken');
                console.log('退出登录时获取的refreshToken:', refreshToken)
                this.$apollo
                    .mutate({
                        mutation: Logout,
                        variables:{
                            refreshToken: refreshToken
                        }
                    })
                    .then(() => {
                        localStorage.setItem('exp', '');
                        localStorage.setItem('email', '');
                        localStorage.setItem('origIat', '');
                        localStorage.setItem('token', '');
                        localStorage.setItem('refreshToken', '');
                        localStorage.setItem('refreshExpiresIn', '');
                        alert('已退出登录并清空存储信息');
                    })
                    .catch((error)=>{
                        alert('退出失败');
                        console.log('退出登录失败原因：',error.message)
                    })
            }
        }
    }
</script>

<style scoped>
    #emailInput {
        position: absolute;
        margin-top: 10px;
        margin-left: 10px;
        width: 30%;
    }

    #userNameInput {
        position: absolute;
        margin-top: 70px;
        margin-left: 10px;
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

    #emailInputLogin {
        position: absolute;
        margin-left: 430px;
        margin-top: 10px;
        width: 30%;
    }

    #pswInputLogin {
        position: absolute;
        margin-left: 430px;
        margin-top: 70px;
        width: 30%;
    }

    #loginBtn {
        position: absolute;
        margin-left: 600px;
        margin-top: 140px;
    }

    #deleteBtn {
        position: absolute;
        margin-left: 590px;
        margin-top: 190px;
    }

    #logoutBtn{
        position: absolute;
        margin-left: 590px;
        margin-top: 240px;
    }
</style>