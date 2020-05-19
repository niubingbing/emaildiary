<template>
    <div class="dropDown">
        <wired-button class="dropBtn">登录</wired-button>
        <div class="dropDownContent">
                <wired-button v-on:click="signIn">
                    登录
                </wired-button>
                <wired-button v-on:click="signIn">
                    注册
                </wired-button>
            <wired-button v-on:click="logout">退出登录</wired-button>
        </div>
    </div>
</template>

<script>
    import Logout from '../../../graphql/user/Logout.graphql';
    import {getToken} from "../../../getToken";

    export default {
        name: "Avatar",
        methods: {
            async logout() {
                const refreshToken = localStorage.getItem('refreshToken');
                console.log('退出登录时获取的refreshToken:', refreshToken);
                if (!await getToken()) {
                    return
                }
                this.$apollo
                    .mutate({
                        mutation: Logout,
                        variables: {
                            refreshToken: refreshToken
                        }
                    })
                    .then(() => {
                        localStorage.setItem('payload', '');
                        localStorage.setItem('token', '');
                        localStorage.setItem('refreshToken', '');
                        localStorage.setItem('refreshExpiresIn', '');
                        alert('已退出登录并清空存储信息');
                    })
                    .catch((error) => {
                        alert('退出失败');
                        console.log('退出登录失败原因：', error.message)
                    })
            },
            signIn(){
                this.$router.push('/signIn')
            }
        }
    }
</script>

<style scoped>
    .dropDown {
        position: absolute;
        margin-top: 1.8%;
        margin-left: 89%;
        display: inline-block;
    }

    .dropBtn {
        cursor: pointer;
        color: black;
    }

    .dropDownContent {
        display: none;
        position: absolute;
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }

    .dropDownContent wired-button {
        text-decoration: none;
        display: block;
    }
    .dropDownContent wired-button:hover{
        background-color: beige;
    }
    .dropDown:hover .dropDownContent{
        display: block;
    }
    .dropDown:hover .dropBtn{
        background-color: aliceblue;
    }
</style>