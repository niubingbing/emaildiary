<template>
    <div id="diary" :style="{ width: screenWidth * 0.8 + 'px', height: screenHeight + 'px'}">
        <wired-button id="btnBack">返回主页</wired-button>
        <!--        暂时添加login登录-->
        <wired-button @click="login">登录</wired-button>
        <!--        暂时添加login登录-->
        <wired-input id="diaryTitleInput" :value="diaryTitle" @input="diaryTitle=$event.target.value"
                     placeholder="日记标题" elevation="2"/>
        <wired-textArea id="diaryTextArea" :value="diaryText" @input="diaryText=$event.target.value"
                        placeholder="记录下你的一天吧" rows="10" elevation="5"/>
        <wired-button id="btnSave" @click="saveDraft" elevation="3">保存</wired-button>
        <wired-button id="btnSend" @click="sendDiary" elevation="3">发送</wired-button>
    </div>
</template>
<script>
    import SendDiary from '../../graphql/diarysend/SendDiary.graphql'
    import Login from '../../graphql/diarysend/Login.graphql'


    let screenHeight = document.documentElement.clientHeight;
    let screenWidth = document.documentElement.clientWidth;


    export default {
        name: 'SendView',
        // 在 `methods` 对象中定义方法
        data() {
            return {
                screenWidth: screenWidth,
                screenHeight: screenHeight,
                diaryTitle: '',
                diaryText: '',
                // TODO 开发时暂时使用，后续修改
                email: '',
                password: ''
            }
        },
        methods: {
            //实现简单的登录
            login() {
                this.$apollo
                    .mutate({
                        mutation: Login,
                        variables: {
                            email: this.email,
                            password: this.password
                        },
                    })
                    .then(result => {
                        window.localStorage['token'] = result.data.tokenAuth.token;
                        alert('登录成功，token已保存。');
                    })
                    .catch((error) => {
                        alert('登录失败。');
                        console.log(error.message);
                    });
            },
            // TODO 保存草稿
            saveDraft: function () {
                alert('功能待完成');
            },
            // 发送日记
            sendDiary: function () {
                this.$apollo
                    .mutate({
                        mutation: SendDiary,
                        variables: {
                            diaryTitle: this.diaryTitle,
                            diaryText: this.diaryText
                        }
                    })
                    .then(() => {
                        console.log('日记发送成功，跳转到主页');
                        this.$router.push({path: '/'});
                    })
                    .catch((error) => {
                        alert('日记发送失败');
                        console.log('日记发送失败：' + error.message);
                    })
            }
        }
    }

</script>


<style scoped>

    #diary {
        font-family: naughty-lite-2, serif;
    }

    #btnBack {
        margin-left: 10%;
    }

    #diaryTitleInput {
        width: 100%;
        margin-left: 10%;
        margin-top: calc(5vh);
    }

    #diaryTextArea {
        width: 100%;
        margin-left: 10%;
        margin-top: calc(5vh);
    }

    #btnSave {
        float: right;
        display: block;
        margin-top: 5%;
    }

    #btnSend {
        float: right;
        display: block;
        margin-top: 5%;
    }
</style>
