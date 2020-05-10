<template>
    <div class="hello">
        <h3 style="z-index: 9">今天心情怎么样呀:)</h3>
        <wired-listbox horizontal selected="two"
                       style="--wired-item-selected-color: darkred; --wired-item-selected-bg: pink; margin: 0">
            <wired-item value="one" role="option">心情大好</wired-item>
            <wired-item value="two">一般一般</wired-item>
            <wired-item value="three">不开心</wired-item>
        </wired-listbox>
    </div>
</template>

<script>
    export default {
        name: "SpiritList"
    }
</script>

<style scoped>
    .hello {
        margin-left: 70%;
        margin-top: 15%;
    }
</style>