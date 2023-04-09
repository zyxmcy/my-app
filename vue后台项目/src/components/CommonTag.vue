<template>
  <div class="tabs">
    <el-tag
      v-for="(tag, index) in tabsList"
      :key="tag.name"
      class="mx-1"
      :closable="tag.name !== 'home'"
      :type="tag.type"
      @click="changeMenu(tag)"
      @close="handleClose(tag, index)"
      :effect="$route.name == tag.name ? 'dark' : 'plain'"
    >
      {{ tag.label }}
    </el-tag>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  computed: {
    ...mapState("tab", ["tabsList"]),
  },
  methods: {
    ...mapMutations("tab", ["closetag"]),
    // 点击tag跳转
    changeMenu(item) {
      this.$router.push(item.name);
    },
    //点击tag删除
    handleClose(item, index) {
      this.closetag(item);
      const len = this.tabsList.length;
      //删除之后路由跳转
      //如果删除的不是选中的
      if (item.name !== this.$route.name) return;

      if (index === len) {
        this.$router.push({
          name: this.tabsList[index - 1].name,
        });
      } else {
        this.$router.push({
          name: this.tabsList[index].name,
        });
      }
    },
  },
  mounted() {},
};
</script>

<style lang="less" scoped>
</style>