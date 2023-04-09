<template>
  <div class="hearder-container">
    <div class="l-content">
      <el-button @click="chengrCollaps" type="primary">
        <el-icon><Grid /></el-icon>
      </el-button>
      <span class="text">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item
            v-for="item in tabsList"
            :key="item.path"
            :to="{ path: item.path }"
            >{{ item.label }}</el-breadcrumb-item
          >
        </el-breadcrumb>
      </span>
    </div>
    <div class="r-content">
      <el-dropdown trigger="click">
        <span class="el-dropdown-link">
          <img src="../images/1.jpg" />
          <el-icon class="el-icon--right"><arrow-down /></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>个人中心</el-dropdown-item>
            <el-dropdown-item @click="logout"> 退出 </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
import { Grid, ArrowDown } from "@element-plus/icons-vue";
import { mapState, mapMutations } from "vuex";
import Cookie from "js-cookie";
export default {
  components: {
    Grid,
    ArrowDown,
  },
  data() {
    return {};
  },
  computed: {
    ...mapState("tab", ["tabsList"]),
  },
  methods: {
    ...mapMutations("tab", ["chengrCollaps"]),
    logout() {
      console.log("退出");
      Cookie.remove("token");
      Cookie.remove("menu");
      this.$router.push("/login");
    },
  },
  mounted() {
    console.log(this.tabsList);
  },
};
</script>
<style lang="less" scoped>
.hearder-container {
  padding-left: 10px;
  background-color: #333;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  .l-content {
    display: flex;
    justify-content: center;
    align-items: center;
    .text {
      color: white;
      font-size: 14px;
      margin-left: 10px;

      /deep/.el-breadcrumb__item {
        .el-breadcrumb__inner {
          color: #666;
          font-weight: normal;
        }
        &:last-child {
          .el-breadcrumb__inner {
            color: white;
          }
        }
      }
    }
  }
}
img {
  width: 40px;
  height: 40px;
}
</style>