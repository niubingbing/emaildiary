<template>
    <div>
        <div v-if="!isRegister">
            <!--        按钮左侧提示用户输入内容的文本-->
            <h3 class="text" id="email">邮箱：</h3>
            <h3 class="text" id="verificationCode">验证码：</h3>
            <h3 class="text" id="name">昵称：</h3>

            <!--        发送验证码按钮-->
            <wired-button id="sendCode" v-on:click="sendCode">发送验证码</wired-button>
            <!--        注册邮箱输入框-->
            <wired-input class="input" id="emailInput" :value="email" @input="email=$event.target.value"
                         placeholder="请输入邮箱"/>
            <!--        验证邮箱格式是否正确，不正确显示提示文本-->
            <div v-if="emailNotValid()">
                <h5 id="emailAttention">
                    * 您的邮箱格式不正确，请检查邮箱格式
                </h5>
            </div>
            <!--        验证码输入框-->
            <wired-input class="input" id="veriCode" :value="veriCode"
                         @input="veriCode=$event.target.value" placeholder="请输入您邮箱中收到的验证码"/>
            <!--        昵称输入框-->
            <wired-input class="input" id="userNameInput" :value="userName" @input="userName=$event.target.value"
                         placeholder="请输入昵称"/>
            <!--下一步按钮-->
            <wired-button id="nextBtn" v-on:click="isRegister=true">
                <div style="width: 100px">
                    下一步
                </div>
            </wired-button>
        </div>
        <div v-else>
            <step-two v-bind:email="email" v-bind:username="userName" v-bind:vericode="veriCode"/>
        </div>

    </div>
</template>

<script>
    import SignUpStepTwo from "./SignUpStepTwo";
    import GetCodeWhenCreate from "../../../graphql/user/GetCodeWhenCreate.graphql"

    export default {
        name: "SignUp",
        data() {
            return {
                email: '',
                veriCode: '',
                userName: '',
                isRegister: false
            }
        },
        components: {
            'step-two': SignUpStepTwo
        },
        methods: {
            emailNotValid() {
                const emailPat = /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/
                return !emailPat.test(this.email);
            },
            sendCode() {
                this.$apollo
                    .mutate({
                        mutation: GetCodeWhenCreate,
                        variables: {
                            email: this.email
                        }
                    })
                    .then(result => {
                        if (result.data.getCodeWhenCreate.success) {
                            alert('验证码已发送')
                        } else {
                            alert('验证码发送失败')
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
    .text {
        position: absolute;
        margin-left: 380px;
    }

    #email {
        margin-top: 24%;
    }

    #verificationCode {
        margin-top: 31%;
        margin-left: 348px;
    }


    #name {
        margin-top: 37%;
    }

    .input {
        position: absolute;
        margin-left: 460px;
        width: 30%;
    }

    #emailInput {
        margin-top: 23%;
    }

    #emailAttention {
        position: absolute;
        margin-top: 28%;
        margin-left: 461px;
        color: red;
    }

    #sendCode {
        position: absolute;
        margin-left: 890px;
        margin-top: 23.5%;
    }

    #sendCode:hover {
        background-color: #6495ED;
    }


    #veriCode {
        margin-top: 30%;
    }

    #userNameInput {
        margin-top: 36%;
    }

    #nextBtn {
        position: absolute;
        margin-top: 42%;
        margin-left: 570px;
    }

    #nextBtn:hover {
        background-color: #6495ED;
    }
</style>