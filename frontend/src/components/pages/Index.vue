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


        <!--        此处暂时添加一个链接跳转到日记编辑界面-->
        <!--    TODO card边框导致边框内部不可点击，调试时点击边框外部-->
        <div >
            <router-link :to="{ name: 'sendDiary' }">sendDiary</router-link>
            <router-view></router-view>
        </div>
        <!--        此处暂时添加一个链接跳转到日记编辑界面-->


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
        name: 'Index',
        data() {
            return {
                msg1: '死生契阔，与子相悦。执子之手，与子偕老',
                msg2: '落红不是无情物，化作春泥更护花',
                msg3: '昔闻洞庭水，今上岳阳楼。吴楚东南坼，乾坤日夜浮。 亲朋无一字，老病有孤舟。 戎马关山北，凭轩涕泗流。',
                msg4: '风急天高猿啸哀，渚清沙白鸟飞回。',
                msg6: '少无适俗韵，性本爱丘山。误落尘网中，一去三十年。羁鸟恋旧林，池鱼思故渊。开荒南野际，守拙归园田。方宅十余亩，' +
                    '草屋八九间。榆柳荫后檐，桃李罗堂前。暧暧远人村，依依墟里烟。',
                msg5: '春花秋月何时了？往事知多少。小楼昨夜又东风，故国不堪回首月明中。',
                msg7: '锦瑟无端五十弦，一弦一柱思华年。庄生晓梦迷蝴蝶，望帝春心托杜鹃。沧海月明珠有泪，蓝田日暖玉生烟。此情可待成追忆，' +
                    '只是当时已惘然。',
                msg8: '大江东去，浪淘尽，千古风流人物。故垒西边，人道是，三国周郎赤壁。乱石穿空，惊涛拍岸，卷起千堆雪。'
            }
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
