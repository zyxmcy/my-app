<template>
  <div class="manage">
    <el-button type="primary" @click="dialogVisible = true"> +新增 </el-button>

    <el-dialog v-model="dialogVisible" title="提示" width="50%" :before-close="handleClose">
      <!-- 用户的表单信息 -->
      <el-form ref="from" :inline="true" :model="from" label-width="80px" class="demo-ruleForm" status-icon
        :rules="rules">
        <el-form-item label="姓名" prop="name">
          <el-input v-model="from.name" placeholder="请输入姓名" />
        </el-form-item>
        <el-form-item label="年龄" prop="age">
          <el-input v-model="from.age" placeholder="请输入年龄" />
        </el-form-item>

        <el-form-item label="性别" prop="sex">
          <el-select v-model="from.sex" placeholder="请选择性别">
            <el-option label="男" value="1" />
            <el-option label="女" value="0" />
          </el-select>
        </el-form-item>
        <el-form-item label="出生日期" prop="birth">
          <div class="block">
            <el-date-picker v-model="from.birth" type="date" placeholder="请选择出生日期" size="default"
              :shortcuts="shortcuts" />
          </div>
        </el-form-item>
        <el-form-item label="地址" prop="address">
          <el-input v-model="from.address" placeholder="请输入地址" />
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
</template>

<script>
export default {
  data() {
    return {
      dialogVisible: false,
      from: {
        name: "",
        age: "",
        sex: "",
        birth: "",
        address: "",
      },
      rules: {
        name: [{ required: true, message: "请输入姓名", trigger: "change" }],
        age: [{ required: true, message: "请输入年龄", trigger: "change" }],
        sex: [{ required: true, message: "请选择性别", trigger: "change" }],
        birth: [{ required: true, message: "请选择日期", trigger: "change" }],
        address: [{ required: true, message: "请输入地址", trigger: "change" }],
      },
      shortcuts: [
        {
          text: "Today",
          value: new Date(),
        },
        {
          text: "Yesterday",
          value: () => {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            return date;
          },
        },
        {
          text: "A week ago",
          value: () => {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            return date;
          },
        },
      ],
    };
  },

  methods: {
    //提交用户表单
    submit() {
      this.$refs.from.validate((valid) => {
        console.log(valid);
        if (valid) {
          console.log(this.from);
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
};
</script>

<style></style>


