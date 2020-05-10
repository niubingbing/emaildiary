<template>
    <div>
        <wired-input id="emailInput" :value="email" @input="email=$event.target.value"></wired-input>
        <wired-input id="userNameInput" :value="userName" @input="userName=$event.target.value"></wired-input>
        <wired-input id="pswInput" :value="psw" @input="psw=$event.target.value"></wired-input>
        <wired-button id="registerBtn" v-on:click="register">注册</wired-button>
<!--        <wired-input></wired-input>-->
<!--        <wired-button id="deleteBtn" v-on:click="del"></wired-button>-->
    </div>
</template>

<script>
    import CreateUser from '../../graphql/user/CreateUser.graphql'

    export default {
        name: "SignInOrUp",
        data() {
            return {
                email: '',
                userName: '',
                psw: ''
            }
        },
        methods: {
            register() {
                alert('注册触发')
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
                    .then(()=>{
                            alert('注册成功')
                    })
                    .catch((error) => {
                        alert(error)
                    })
            }
        }
    }
</script>

<style scoped>

</style>