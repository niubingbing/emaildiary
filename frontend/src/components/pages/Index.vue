<template>
    <div>
        <!--        跳转去日记编写页面的按钮-->
        <router-link to="/edit">
            <wired-fab class="CreateDiaryButton">
                <font-awesome-icon icon="pencil-alt"/>
            </wired-fab>
        </router-link>
        <!--        跳转去日记编写页面的按钮结束-->

        <!--        跳转去设置页面-->
        <router-link to="/set">
            <wired-button id="setBtn">资料设置</wired-button>
        </router-link>
        <!--        跳转去设置页面结束-->

        <div class="box">
            <!--        网页的边框-->
            <wired-card class="frame" elevation="5"/>
            <!--        网页的边框结束-->

            <!--            显示最近 16 条日记的列表-->
            <index-diary></index-diary>
            <!--            显示最近 16 条日记的列表结束-->


            <!--             TODO: 后期要把这四个按钮做成一个下拉列表，登录/注册单独成页面，注销账号放在设置页面中-->
            <!--           跳转到登录/登出/注册/注销页面-->
            <router-link to="/signIn">
                <index-avatar></index-avatar>
            </router-link>
            <!--            跳转到登录/登出/注册/注销页面-->

            <!--            日历-->
            <!--            <index-calendar></index-calendar>-->
            <!--            选择心情的列表-->
            <index-spirit></index-spirit>
        </div>

    </div>
</template>

<script>
    import DiaryList from "./IndexComponents/DiaryList";
    import Avatar from "./IndexComponents/Avatar";
    import SpiritList from "./IndexComponents/SpiritList";
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {faPencilAlt} from '@fortawesome/free-solid-svg-icons'


    library.add(faPencilAlt)


    export default {
        name: 'Index',
        components: {
            'index-diary': DiaryList,
            'index-avatar': Avatar,
            'index-spirit': SpiritList,
        }
    }
</script>

<style scoped>

    .box {
        position: absolute;
        height: 80%;
        width: 90%;
        padding: 0;
        margin-top: 5%;
        margin-left: 5%;
        border: 0;
    }

    .CreateDiaryButton {
        position: absolute;
        height: 90px;
        width: 90px;
        margin-left: 7%;
        margin-top: 1%;
        --wired-fab-bg-color: pink;
    }

    #setBtn {
        position: absolute;
        margin-left: 200px;
        margin-top: 1%;
    }

    .frame {
        position: absolute;
        height: 100%;
        width: 100%;
        padding: 0;
        margin: 0;
        z-index: 0;
    }
</style>