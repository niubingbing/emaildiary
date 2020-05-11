<template>
    <div>
        <router-link to="/edit">
            <wired-fab class="CreateDiaryButton">
                <font-awesome-icon icon="pencil-alt"/>
            </wired-fab>
        </router-link>
        <div class="box">
            <!--        网页的边框-->
            <wired-card class="frame" elevation="5"/>
            <index-diary></index-diary>
            <router-link to="/signIn">
                <index-avatar></index-avatar>
            </router-link>
            <!--            <index-calendar></index-calendar>-->
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

    .frame {
        position: absolute;
        height: 100%;
        width: 100%;
        padding: 0;
        margin: 0;
        z-index: 0;
    }
</style>