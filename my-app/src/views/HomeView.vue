<template>
  <div>
    <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="item in 3" :key="item">
      <img src="../images/slideshow1.jpeg" v-if="item==1" @click="zodiac">
      <img src="../images/slideshow2.jpeg" v-if="item==2" @click="">
      <img src="../images/slideshow3.jpeg" v-if="item==3">
    </el-carousel-item>
  </el-carousel>

  中国传统文化发展历程
  <el-steps :active="5" align-center>
  <el-step title="一、前文明期：猿人到大禹传子" description="这是中国文化的史前期，它包括旧石器时代和新石器时代，相当于中国古史的传说时代。"></el-step>
  <el-step title="二、雏形期：夏、商、西周至春秋、战国" description="尽管这一时期华夏组的宏大空间（“中国”）还很有限，尚没有对南北四方产生足够的作用力，但中国文明的基石已初步奠定，象形会意的汉字、儒墨道法等诸子思想、伦理宗法等等都对后世影响甚巨。"></el-step>
  <el-step title="三、定型期：秦汉" description="如果向前追溯，一统帝国文化的端绪应该溯源至春秋战国之际，因为其时所发生的第一次社会大变革和文化大转型，已经寓合着政治的大一统和文化的大一统。"></el-step>
  <el-step title="四、融合期：魏晋南北朝至唐中叶" description="这一时期，与庄园经济和门阀贵族政治相表里，精神领域里神学弥漫，儒、道、玄、佛各擅胜场，影响着思想意识各文化门类。"></el-step>
  <el-step title="五、强化期：唐中叶至明中叶" description="唐代前后期的转折，规范了中国文化史后半段的大致框架。唐宋以降的一年间，中国文化在自身的发展中，总体上已显示出走出中古文化故辙的种种动向，韵语了部分近世文化因子，可以称之为近古文化期。"></el-step>
  <el-step title="六、转型期：明末迄今" description="这一阶段，已先期完成现代转型的工业西方以炮舰加商品打开了中国封闭的国门。中国文化第一次遭遇到“高势位”文化的入侵，中国文化与西方文化的冲突、调适、融合过程异常艰难也异常痛苦，中国文化在制度、物质、行为、精神诸层面进入现代转型期。"></el-step>
</el-steps>
  </div>
  <el-header><Aside/></el-header>
</template>

<script>
import Aside from '@/components/Aside.vue';

  export default {
    data() {
        return {};
    },
    methods: {
        zodiac() {
            this.$router.push("/");
        }
    },
    components: { Aside }
}
</script>

<style scoped>
img{
  width: 100%;
  height: inherit;
}
</style>