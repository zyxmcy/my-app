<template>
  <!-- <div class="layout">
    <el-container>
      <el-aside width="auto"></el-aside>
      <el-container>
        <el-header><Header /></el-header>
        <el-main><router-view></router-view></el-main>
        <el-footer> <Aside /> </el-footer>
      </el-container>
    </el-container> -->
  <!-- </div> -->
  <div class="common-layout">
    <el-container>
      <el-header><Header/></el-header>
      <!-- <el-header><Aside/></el-header> -->
      <el-main><router-view></router-view></el-main>
    </el-container>
  </div>
</template>


<script>
import Flooter from "@/components/Flooter.vue";
import Aside from "../components/Aside.vue";
import Header from "../components/Header.vue";


export default {
  components: { Aside, Header,  Flooter },
};
</script>

<style lang="less" scoped>
.el-header {
  padding: 0;
}
</style>