<template>
    <wired-icon-button class="icon"><img src="https://picture-1301351492.cos.ap-beijing.myqcloud.com/icon.jpg"
                                         class="picture"></wired-icon-button>
</template>

<script>
    export default {
        name: "Avatar"
    }
</script>

<style scoped>
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
</style>