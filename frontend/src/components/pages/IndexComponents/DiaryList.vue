<template>
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
</template>

<script>
    export default {
        name: "DiaryList",
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
    wired-card.diary1 {
        position: absolute;
        height: 40%;
        margin-top: 1%;
        width: 13%;
        margin-left: 0;
        border: 0;
    }

    wired-card.diary2 {
        position: absolute;
        height: 55%;
        margin-top: 25%;
        width: 13%;
        margin-left: 0;
        border: 0;
    }

    wired-card.diary3 {
        position: absolute;
        height: 60%;
        margin-top: 1%;
        width: 13%;
        margin-left: 17%;
        border: 0;
    }

    wired-card.diary4 {
        position: absolute;
        height: 34%;
        margin-top: 36%;
        width: 13%;
        margin-left: 17%;
        border: 0;
    }

    wired-card.diary5 {
        position: absolute;
        height: 25%;
        margin-top: 1%;
        width: 13%;
        margin-left: 34%;
        border: 0;
    }

    wired-card.diary6 {
        position: absolute;
        height: 67%;
        margin-top: 18%;
        width: 13%;
        margin-left: 34%;
        border: 0;
    }

    wired-card.diary7 {
        position: absolute;
        height: 43%;
        margin-top: 1%;
        width: 13%;
        margin-left: 51%;
        border: 0;
    }

    wired-card.diary8 {
        position: absolute;
        height: 50%;
        margin-top: 27%;
        width: 13%;
        margin-left: 51%;
        border: 0;
    }
</style>