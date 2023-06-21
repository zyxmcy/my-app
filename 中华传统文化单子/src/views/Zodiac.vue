<template>
  <el-row>
  <el-col :span="4" v-for="(o, index) in 12" :key="o" >
    <el-card @click="tiao" :body-style="{ padding: '0px' }">
      <img v-if="index==0" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2F28ef5d9b608d93f4391b49b11f11376c.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=038a5bffd2fd8dbab8d9c2128469bb39" class="image">
      <img v-if="index==1" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2F69ecd16ab08cc87e74c46f335bc6d07a.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=6523eab8f4bdd11f43c72e4892163a57" class="image">
      <img v-if="index==2" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2Fc54ac2241a01b2e086799b25560a368b.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=a310e0ba8fc25607dbcb5f81712a5ed1" class="image">
      <img v-if="index==3" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2F6e53894e30cc3494653671ecf6826a8a.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=59c8f619144c6205aee90faf1a830241" class="image">
      <img v-if="index==4" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2F09d10ec525929b3b0d59d65e3ce3101c.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=dfed74994dd28ab5a0c0e689ac872eea" class="image">
      <img v-if="index==5" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2F6ef29d72f2cee9fab1d68a5eac3ec973.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=4412ad15d52d40412cf029079fe36a44" class="image">
      <img v-if="index==6" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2F68e1089ded2dfe998e5c210d6aa1ab02.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=6c775673a98665047b47c72557334746" class="image">
      <img v-if="index==7" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2F5aac40511e25d8a661cfb9cd967eef8f.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=ab68d9c201f466d4b1cd8557933c31d1" class="image">
      <img v-if="index==8" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2Fffd598e95838b536551d64ae7aaf02e4.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=58294953c12b4b45680950394fd9a47e" class="image">
      <img v-if="index==9" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2Fed66b5171187f41033fa43f9ca6ba4ce.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=7d9a2d479d5acdff0d645464f73d1ae3" class="image">
      <img v-if="index==10" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2F0fa228dae39246689522c892d25f9179.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=1ce98bfd5d1b773149f0426a7d9ee2dd" class="image">
      <img v-if="index==11" src="https://gimg3.baidu.com/search/src=https%3A%2F%2Fsearch-operate.cdn.bcebos.com%2Fc8b50d82e8287107909ca91cb79a7331.png&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=w621&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1673542800&t=28596a98e4d130042f5606f4b0559c63" class="image">
      <div style="padding: 14px;">
        <span v-if="index==0">子鼠</span>
        <span v-if="index==1">丑牛</span>
        <span v-if="index==2">寅虎</span>
        <span v-if="index==3">卯兔</span>
        <span v-if="index==4">辰龙</span>
        <span v-if="index==5">巳蛇</span>
        <span v-if="index==6">午马</span>
        <span v-if="index==7">未羊</span>
        <span v-if="index==8">申猴</span>
        <span v-if="index==9">酉鸡</span>
        <span v-if="index==10">戌狗</span>
        <span v-if="index==11">戌狗</span>
        <div class="bottom clearfix">
          <time class="time">{{ currentDate }}</time>
     
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>
<el-header><Aside/></el-header>
</template>

<script>
import Aside from '@/components/Aside.vue';

export default {
    data() {
        return {
            currentDate: new Date()
        };
    },
    methods: {
        tiao() {
            if (Math.random(1) >= 0.5)
                window.location.href = "https://baike.baidu.com/item/åäºçè/48593";
            window.open("https://baike.baidu.com/item/åäºçè/48593");
        }
    },
    components: { Aside }
};
</script>

<style scoped>
  .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>