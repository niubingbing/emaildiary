<template>
    <div id="app">
        <MainInterface :msg1="msg1" :msg2="msg2" :msg3="msg3" :msg4="msg4" :msg5="msg5" :msg6="msg6" :msg7="msg7" :msg8="msg8"/>
    </div>
</template>

<script>
    import MainInterface from '@/components/MainInterface';

    export default {
        name: 'App',
        components: {
            MainInterface
        },
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

<style>
    @font-face {
        font-family: naughty-lite-2;
        src: url('./assets/fangzhengjinglei.ttf');

    }

    #app {
        font-family: naughty-lite-2, serif;
        font-size: 1.5em;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        margin: 0;
        padding: 0;
        height: 100%;
        width: 100%;
    }
</style>
