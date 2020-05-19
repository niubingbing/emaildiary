<template>
    <div>
        <!--        登录控件-->
        <wired-input id="emailInputLogin" :value="emailLogin" @input="emailLogin=$event.target.value"
                     placeholder="请输入登录邮箱"/>
        <div v-if="emailNotValid()">
            <h5 id="emailAttention">
                * 您的邮箱格式不正确，请检查邮箱格式
            </h5>
        </div>
        <wired-input type="password" id="pswInputLogin" :value="pswLogin" @input="pswLogin=$event.target.value"
                     placeholder="请输入登录密码"/>
        <wired-button id="loginBtn" v-on:click="login">
            <div style="width: 100px">
                登录
            </div>
        </wired-button>
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
            emailNotValid() {
                const pat = /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/
                return !pat.test(this.emailLogin);
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
        margin-left: 432px;
        margin-top: 23%;
        width: 30%;
    }

    #emailAttention{
        position: absolute;
        margin-left: 433px;
        margin-top: 28%;
        color: red;
    }

    #pswInputLogin {
        position: absolute;
        margin-left: 432px;
        margin-top: 30%;
        width: 30%;
    }

    #loginBtn {
        position: absolute;
        margin-left: 555px;
        margin-top: 37%;
    }

    #loginBtn:hover {
        background-color: #6495ED;
    }
</style>