<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: 'App'
    }
</script>

<style>
    @font-face {
        font-family: naughty-lite-2;
        src: url('assets/fonts/fangzhengjinglei.ttf');

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
