<template>
    <div style="width: 100%; height: 100%">
        <wired-card id="box" elevation="4"></wired-card>
        <wired-card id="background" fill="#6495ED">
        </wired-card>
        <img src="../../assets/images/logo3.png" id="logo">
        <wired-button id="inBtn" v-on:click="sUp=false" elevation="4">
            <div style="width: 200px">
                登录
            </div>
        </wired-button>
        <wired-button id="upBtn" v-on:click="sUp=true" elevation="4">
            <div style="width: 200px">
                注册
            </div>
        </wired-button>
        <div v-if="sUp">
            <sign-up></sign-up>
        </div>
        <div v-else>
            <sign-in></sign-in>
        </div>
        <img src="../../assets/images/boy.png" id="boy">
        <img src="../../assets/images/girl.png" id="girl">
    </div>
</template>

<script>
    import SignIn from "./SignComponents/SignIn";
    import SignUp from "./SignComponents/SignUp";

    export default {
        name: "SignInOrUp",
        data() {
            return {
                sUp: false
            }
        },
        components: {
            'sign-in': SignIn,
            'sign-up': SignUp
        }
    }
</script>

<style scoped>
    #box {
        position: absolute;
        width: 90.2%;
        height: 92.2%;
        margin-left: 4.99%;
        margin-top: 0.99%;
        z-index: -1;
    }

    #background {
        position: absolute;
        width: 90%;
        height: 92%;
        margin-left: 5%;
        margin-top: 1%;
        z-index: -1;
        opacity: 0.5;
    }

    #inBtn {
        position: absolute;
        margin-left: 28%;
        margin-top: 20%;
    }

    #inBtn:hover {
        background-color: #6495ED;
    }

    #upBtn {
        position: absolute;
        margin-left: 55%;
        margin-top: 20%;
    }

    #upBtn:hover {
        background-color: #6495ED;
    }

    #logo {
        position: absolute;
        width: 50%;
        height: 15%;
        margin-top: 10%;
        margin-left: 25%;

    }

    .inOrUp {
        position: absolute;
    }

    #boy {
        position: absolute;
        margin-left: 6%;
        width: 15%;
        margin-top: 32.5%;
    }

    #girl{
        position: absolute;
        margin-left: 80%;
        width: 15%;
        margin-top: 32%;
    }
</style>