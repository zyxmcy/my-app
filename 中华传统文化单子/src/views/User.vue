<template>
  <div class="manage">
    <el-button type="primary" @click="dialogVisible = true"> +新增 </el-button>

    <el-dialog
      v-model="dialogVisible"
      title="提示"
      width="50%"
      :before-close="handleClose"
    >
      <!-- 用户的表单信息 -->
      <el-form
        ref="from"
        :inline="true"
        :model="from"
        label-width="80px"
        class="demo-ruleForm"
        status-icon
        :rules="rules"
      >
        <el-form-item label="title" prop="title">
          <el-input v-model="from.title" placeholder="请输入成语" />
        </el-form-item>
        <el-form-item label="text" prop="text">
          <el-input v-model="from.text" placeholder="请描述一下" />
        </el-form-item>

      </el-form>

      <template #footer>
        <span class="dialog-footer">
          <el-button @click="cancel">关闭</el-button>
          <el-button type="primary" @click="submit"> 确定 </el-button>
        </span>
      </template>
    </el-dialog>
  </div>

  <el-collapse v-for="(item, index) in person" :key="item.title">
    <el-collapse-item :title="item.title" name="1">
      <div> {{ item.text }}</div>
    </el-collapse-item>
  </el-collapse>
  <el-header><Aside/></el-header>
</template>

<script>
import Aside from '@/components/Aside.vue';

export default {
    data() {
        return {
            person: [
                {
                    title: "管鲍之交",
                    text: "春秋战国时期，管仲和鲍叔牙是合作关系，开始的时候管仲并不得志无论是做买卖还是做事鲍叔牙始终相信他，并给了他竭尽所能的照顾，到最后管仲封侯拜相.管仲对周围的人说，生我的是父母，了解我的是鲍叔牙。这才是我的好朋友啊！是人用这个成语形容两个人的良好的友谊，也是形容对朋友的信任"
                },
                {
                    title: "背水一战",
                    text: "楚汉相争的时候，刘邦命手下大将韩信领兵攻打赵国。赵王带了二十万大军在太行山的井陉关迎击。当时，韩信只带了一万二千人马。为了打败赵军，他将一万人驻扎在河边列了一个背水阵。另外派两千轻骑潜伏在赵军军营周围。交战后，赵营二十万大军向河边的一万汉军杀来。汉军面临大敌，后无退路，只能拼死奋战。这时潜伏的那两千士兵乘虚攻进赵营。赵军遭到前后夹击，很快被韩信打败。战后有人问韩信：“背水列阵乃兵家大忌，将军为何明知故犯？”韩信笑着说：“置之死地而后生，这也是兵书上有记载的呀。”"
                },
                {
                    title: "晏子使楚",
                    text: "春秋末期，齐国大夫晏子出使楚国，楚王三次侮辱晏子，想显示楚国的威风，晏子巧妙回击，维护了自己和国家尊严的故事。故事赞扬了晏子爱国，机智勇敢，善于辞令。灵活善辩的外交才能与不惧大国、不畏强暴的斗争精神。讽刺了狂妄自大，傲慢无理，自作聪明的人。"
                }
            ],
            dialogVisible: false,
            from: {
                title: "",
                text: "",
            },
            rules: {
                title: [{ required: true, message: "请输入成语", trigger: "change" }],
                text: [{ required: true, message: "请描述一下", trigger: "change" }],
            },
        };
    },
    methods: {
        addperson(from) {
            this.person.unshift(from);
        },
        //提交用户表单
        submit() {
            this.$refs.from.validate((valid) => {
                console.log("valid", valid);
                if (valid) {
                    console.log("this.from", this.from);
                    console.log(this.from.text);
                    console.log(this.from.title);
                    this.addperson({ title: this.from.title, text: this.from.text });
                    this.$refs.from.resetFields();
                    this.dialogVisible = false;
                }
            });
        },
        //清空from表单
        handleClose() {
            this.$refs.from.resetFields();
            this.dialogVisible = false;
        },
        cancel() {
            this.handleClose();
        },
    },
    components: { Aside }
};
</script>

<style>

</style>


