<template>
    <div>
        <h3 class="text" id="password">密码：</h3>
        <h3 class="text" id="passwordConfirm">确认密码：</h3>
        <!--        密码输入框-->
        <wired-input class="input" type="password" id="pswInput" :value="psw" @input="psw=$event.target.value"
                     placeholder="请输入密码"/>
        <!--        验证密码是否正确，不正确显示提示文本-->
        <div v-if="pswNotValid()">
            <h5 id="passwordAttention">
                * 请输入8到30位密码，格式为数字、大写字母、小写字母、半角字符四选三
            </h5>
        </div>
        <!--        确认密码输入框-->
        <wired-input class="input" type="password" id="pswConfirmInput" :value="pswConfirm"
                     @input="pswConfirm=$event.target.value" placeholder="请再次输入密码"/>
        <!--        验证两次密码是否一致，不一致显示提示文本-->
        <div v-if="pswNotSame()">
            <h5 id="pswSameAttention">
                * 两次密码不一致
            </h5>
        </div>
        <!--注册按钮-->
        <wired-button id="registerBtn" v-on:click="register">
            <div style="width: 100px">
                注册
            </div>
        </wired-button>
    </div>
</template>

<script>
    import CreateUser from "../../../graphql/user/CreateUser.graphql";

    export default {
        name: "SignUpStepTwo",
        data() {
            return {
                psw: '',
                pswConfirm: '',
            }
        },
        props:{
            email: String,
            vericode: String,
            username: String
        },
        methods: {
            pswNotValid() {
                const pswPat = /^(?![a-zA-Z]+$)(?![A-Z0-9]+$)(?![A-Z\W_!@#$%^&*`~()-+=]+$)(?![a-z0-9]+$)(?![a-z\W_!@#$%^&*`~()-+=]+$)(?![0-9\W_!@#$%^&*`~()-+=]+$)[a-zA-Z0-9\W_!@#$%^&*`~()-+=]{8,30}$/
                return !pswPat.test(this.psw);
            },
            pswNotSame() {
                return this.psw !== this.pswConfirm;
            },
            register() {
                console.log(this.email, this.username, this.psw, this.vericode)
                this.$apollo
                    .mutate({
                        mutation: CreateUser,
                        variables: {
                            email: this.email,
                            name: this.username,
                            password: this.psw,
                            code: this.vericode
                        }
                    })
                    .then(result => {
                        if (result.data.createUser.success) {
                            alert('注册成功')
                            this.$router.push('./signIn')
                        } else {
                            alert('注册失败')
                        }
                    })
                    .catch((error) => {
                        console.log(error.message)
                        return false
                    })
            }
        }
    }
</script>

<style scoped>
    .text {
        position: absolute;
        margin-left: 380px;
    }

    #password {
        margin-top: 24%;
    }

    #passwordConfirm {
        margin-left: 323px;
        margin-top: 31%;
    }

    .input {
        position: absolute;
        margin-left: 460px;
        width: 30%;
    }


    #pswInput {
        margin-top: 23%;
    }

    #passwordAttention {
        position: absolute;
        margin-left: 461px;
        margin-top: 28%;
        color: red;
        z-index: 9;
    }

    #pswConfirmInput {
        margin-top: 30%;
    }

    #pswSameAttention {
        position: absolute;
        margin-left: 461px;
        margin-top: 35%;
        color: red;
        z-index: 9;
    }

    #registerBtn {
        position: absolute;
        margin-left: 565px;
        margin-top: 38%;
    }

    #registerBtn:hover {
        background-color: #6495ED;
    }

</style>