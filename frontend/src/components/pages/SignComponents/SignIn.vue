<template>
    <div>
        <!--        登录控件-->
        <wired-input id="emailInputLogin" :value="emailLogin" @input="emailLogin=$event.target.value"
                     placeholder="请输入登录邮箱"/>
        <wired-input type="password" id="pswInputLogin" :value="pswLogin" @input="pswLogin=$event.target.value"
                     placeholder="请输入登录密码"/>
        <wired-button id="loginBtn" v-on:click="login">登录</wired-button>
        <!--        登录控件-->
    </div>
</template>

<script>
    import Login from '../../../graphql/user/Login.graphql'

    export default {
        name: "SignIn",
        data() {
            return {
                emailLogin: '',
                pswLogin: ''
            }
        },
        methods: {
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
                        localStorage.setItem('payload', JSON.stringify(result.data.tokenAuth.payload))
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
            }
        }
    }
</script>

<style scoped>
    #emailInputLogin {
        position: absolute;
        margin-left: 430px;
        margin-top: 25%;
        width: 30%;
    }

    #pswInputLogin {
        position: absolute;
        margin-left: 430px;
        margin-top: 32%;
        width: 30%;
    }

    #loginBtn {
        position: absolute;
        margin-left: 600px;
        margin-top: 37%;
    }
</style>