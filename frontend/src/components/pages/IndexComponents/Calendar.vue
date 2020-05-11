<template>
    <div class="calendar-box">
        <wired-calendar selected="Apr 8, 2020" class="calendar"></wired-calendar>
    </div>
</template>

<script>
    export default {
        name: "Calendar"
    }
</script>

<style scoped>
    .calendar-box {
        position: absolute;
        height: 100%;
        width: 100%;
        padding: 0;
        margin: 0;
    }

    wired-calendar.calendar {
        position: absolute;
        margin-top: 10%;
        margin-left: 68%;
    }

</style>