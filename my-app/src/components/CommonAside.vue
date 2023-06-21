<template>
  <div>
    <el-menu
      active-text-color="#ffd04b"
      background-color="#545c64"
      class="el-menu-vertical-demo"
      default-active="2"
      text-color="#fff"
      @open="handleOpen"
      @close="handleClose"
      :collapse="isCollaps"
    >
      <h3>{{ isCollaps ? "后台" : "后台管理系统" }}</h3>
      <el-menu-item
        @click="clickMenu(item)"
        v-for="item in noChildren"
        :key="item.name"
        :index="item.name"
      >
        <el-icon><component :is="item.icon"></component></el-icon>
        <template #title>{{ item.label }}</template>
      </el-menu-item>

      <el-sub-menu
        v-for="item in haveChildren"
        :key="item.lable"
        :index="item.label"
      >
        <template #title>
          <el-icon><component :is="item.icon"></component></el-icon>
          <span>{{ item.label }}</span>
        </template>
        <el-menu-item-group>
          <template #title><span>Group One</span></template>
          <el-menu-item
            v-for="item2 in item.children"
            :key="item2.name"
            :index="item2.name"
            @click="chengepage(item2)"
            >{{ item2.label }}</el-menu-item
          >
        </el-menu-item-group>
      </el-sub-menu>
    </el-menu>
  </div>
</template>

<script>
import { markRaw } from "vue";
import { mapState, mapMutations } from "vuex";
import {
  Menu as IconMenu,
  Location,
  VideoPlay,
  Avatar,
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
  },
  data() {
    return {
      // menu: [
      //   {
      //     path: "/",
      //     name: "home",
      //     label: "首页",
      //     icon: markRaw(House),
      //     url: "Home/Home",
      //   },
      //   {
      //     path: "/mall",
      //     name: "mall",
      //     label: "商品管理",
      //     icon: markRaw(VideoPlay),
      //     url: "MallManage/MallManage",
      //   },
      //   {
      //     path: "/user",
      //     name: "user",
      //     label: "用户管理",
      //     icon: markRaw(Avatar),
      //     url: "UserManage/UserManage",
      //   },
      //   {
      //     label: "其他",
      //     icon: markRaw(Location),
      //     children: [
      //       {
      //         path: "/pageOne",
      //         name: "pageOne",
      //         label: "页1",
      //         icon: "setting",
      //         url: "Other/PageOne",
      //       },
      //       {
      //         path: "/PageTwo",
      //         name: "pageTwo",
      //         label: "页2",
      //         icon: "setting",
      //         url: "Other/PageTwo",
      //       },
      //     ],
      //   },
      // ],
    };
  },

  methods: {
    ...mapMutations("tab", ["selectMenu"]),
    clickMenu(item) {
      this.$router.push(item.path);
      this.selectMenu(item);
    },
    chengepage(item2) {
      this.$router.push(item2.path);
      this.selectMenu(item2);
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
  computed: {
    ...mapState("tab", ["isCollaps","menu"]),
    menu(){
      return JSON.parse(Cookie.get('menu'))
    },
    noChildren() {
      return this.menu.filter((x) => !x.children);
    },
   
    haveChildren() {
      return this.menu.filter((x) => x.children);
    },
  },
};
</script>

<style lang="less" scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  // width: 200px;
  min-height: 400px;
}
.el-menu {
  height: 100vh;
  h3 {
    color: #fff;
    text-align: center;
    line-height: 48px;
    font-size: 16px;
    font-weight: 400;
  }
}
</style>
