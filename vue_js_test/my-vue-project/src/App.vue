<script setup>
import http from './api/axios_test_01'
http.then((data) => {
    data = data.data.data
    // 处理data数据
    // 1.统计年龄相同的人的数量
    // 2.  求年龄相同的人的salary的和
    // 3. 求各个年龄段的人的salary的平均值----20-30,30-40,40-50,50-60
    console.log(data);
})


</script>

<template>
    <!-- this is the html area -->
</template>

<style scoped></style>
