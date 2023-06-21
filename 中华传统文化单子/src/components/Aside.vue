<template>

    <el-menu active-text-color="#ffd04b" background-color="skyblue" class="el-menu-vertical-demo" default-active="2"
      text-color="pink" @open="handleOpen" :collapse="isCollaps" mode="horizontal">
      <el-menu-item @click="clickMenu(item)" v-for="item in noChildren" :key="item.name" :index="item.name">
        <el-icon>
          <component :is="item.icon"></component>
        </el-icon>
        <template #title>{{ item.label }}</template>
      </el-menu-item>
    </el-menu>

</template>

<script>
import { mapState, mapMutations } from "vuex";
import {
  Menu as IconMenu,
  Location,
  VideoPlay,
  Avatar,
  Picture,
  House,
} from "@element-plus/icons-vue";
import Cookie from "js-cookie";
export default {
  components: {
    IconMenu,
    Location,
    VideoPlay,
    Avatar,
    House,
    Picture
  },
  methods: {
    ...mapMutations("tab", ["selectMenu"]),
    clickMenu(item) {
      this.$router.push(item.path);
      this.selectMenu(item);
    },

    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },

  },
  computed: {
    ...mapState("tab", ["isCollaps", "menu"]),
    menu() {
      return JSON.parse(Cookie.get('menu'))
    },
    noChildren() {
      return this.menu.filter((x) => !x.children);
    },
  },
};
</script>

<style lang="less" scoped>
.el-menu-vertical-demo{
  display: flex;
  justify-content: space-between;
  width: 100%;
}
h3 {
    color: #fff;
    text-align: center;
    line-height: 48px;
    font-size: 16px;
    font-weight: 400;
  }
</style>
