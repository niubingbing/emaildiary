<template>
    <div class="box">
        <!--        网页的边框-->
        <wired-card class="card">
        </wired-card>
        <h3 class="hello">今天心情怎么样呀:)</h3>
        <div class="mind">
            <wired-listbox horizontal selected="two"
                           style="--wired-item-selected-color: darkred; --wired-item-selected-bg: pink;">
                <wired-item value="one" role="option">心情大好</wired-item>
                <wired-item value="two">一般一般</wired-item>
                <wired-item value="three">不开心</wired-item>
            </wired-listbox>
        </div>
        <!--存储日记的box-->
        <div class="box">
            <wired-card fill="#FFB6C1" elevation="3" class="diary1">
                <div align="center" style="text-overflow: clip">{{msg1}}</div>
            </wired-card>
            <wired-card fill="#6495ED" elevation="3" class="diary2">
                <div align="center" style="text-overflow: clip">{{msg2}}</div>
            </wired-card>
            <wired-card fill="#7FFFAA" elevation="3" class="diary3">
                <div align="center" style="text-overflow: clip">{{msg3}}</div>
            </wired-card>
            <wired-card fill="#BA55D3" elevation="3" class="diary4">
                <div align="center" style="text-overflow: clip">{{msg4}}</div>
            </wired-card>
            <wired-card fill="#FAFAD2" elevation="3" class="diary5">
                <div align="center" style="text-overflow: clip">{{msg5}}</div>
            </wired-card>
            <wired-card fill="#FFA07A" elevation="3" class="diary6">
                <div align="center" style="text-overflow: clip">{{msg6}}</div>
            </wired-card>
            <wired-card fill="#A9A9A9" elevation="3" class="diary7">
                <div align="center" style="text-overflow: clip">{{msg7}}</div>
            </wired-card>
            <wired-card fill="#B0C4DE" elevation="3" class="diary8">
                <div align="center" style="text-overflow: clip">{{msg8}}</div>
            </wired-card>
        </div>
        <!--存储日历的box-->
        <div class="calendar-box">
            <wired-calendar selected="Apr 8, 2020" class="calendar"></wired-calendar>
            <wired-icon-button class="icon"><img src="https://picture-1301351492.cos.ap-beijing.myqcloud.com/icon.jpg"
                                                 class="picture"></wired-icon-button>
            <img src="https://picture-1301351492.cos.ap-beijing.myqcloud.com/EmailDiary.png" class="logo">
        </div>
    </div>
</template>

<script>
    export default {
        name: 'MainInterface',
        props: {
            msg1:String,
            msg2: String,
            msg3: String,
            msg4: String,
            msg5: String,
            msg6: String,
            msg7: String,
            msg8: String
        }
    }
</script>

<style scoped>
    .hello {
        position: absolute;
        margin-left: 5%;
        margin-top: 2%;
    }

    .mind {
        position: absolute;
        margin-left: 25%;
        margin-top: 1%;
    }

    .box {
        position: absolute;
        height: 100%;
        width: 100%;
        padding: 0;
        margin: 0;
    }

    .calendar-box {
        position: absolute;
        height: 100%;
        width: 100%;
        padding: 0;
        margin: 0;
    }

    wired-card.card {
        position: absolute;
        height: 99%;
        width: 98%;
        padding: 0;
        margin-left: 1%;
        margin-top: 0.5%;
        border: 0;
    }

    wired-card.diary1 {
        position: absolute;
        height: 40%;
        margin-top: 5%;
        width: 13%;
        margin-left: 3%;
        border: 0;
    }

    wired-card.diary2 {
        position: absolute;
        height: 42%;
        margin-top: 29%;
        width: 13%;
        margin-left: 3%;
        border: 0;
    }

    wired-card.diary3 {
        position: absolute;
        height: 60%;
        margin-top: 5%;
        width: 13%;
        margin-left: 19%;
        border: 0;
    }

    wired-card.diary4 {
        position: absolute;
        height: 22%;
        margin-top: 39.5%;
        width: 13%;
        margin-left: 19%;
        border: 0;
    }

    wired-card.diary5 {
        position: absolute;
        height: 25%;
        margin-top: 5%;
        width: 13%;
        margin-left: 35%;
        border: 0;
    }

    wired-card.diary6 {
        position: absolute;
        height: 56.5%;
        margin-top: 21%;
        width: 13%;
        margin-left: 35%;
        border: 0;
    }

    wired-card.diary7 {
        position: absolute;
        height: 43%;
        margin-top: 5%;
        width: 13%;
        margin-left: 51%;
        border: 0;
    }

    wired-card.diary8 {
        position: absolute;
        height: 39%;
        margin-top: 30.5%;
        width: 13%;
        margin-left: 51%;
        border: 0;
    }

    wired-calendar.calendar {
        position: absolute;
        margin-top: 10%;
        margin-left: 68%;
    }

    .icon {
        position: absolute;
        margin-top: 1.8%;
        margin-left: 89%;
    }

    .picture {
        height: 85px;
        width: 85px;
        border-radius: 50%;
    }

    .logo {
        position: absolute;
        height: 85px;
        width: 250px;
        margin-top: 3%;
        margin-left: 69%;
    }

</style>