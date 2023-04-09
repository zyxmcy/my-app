<template>
  <el-form label-width="70px" class="login-container" :model="form" :rules="rules">
    <h3 class="login_title">系统登录</h3>
    <el-form-item label="用户名" prop="username">
      <input placeholder="请输入名称" v-model="form.user" />
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <input type="password" placeholder="请输入密码" v-model="form.pwd" />
    </el-form-item>
    <el-form-item>
      <el-button @click="submit" style="margin-left: -60px; margin-top: 10px" type="primary">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import Mock from "mockjs";
import Cookie from "js-cookie";
import { reactive } from "vue";
import router from "@/router";
import {getMenu} from '../api/module/first'
import { ElMessage } from 'element-plus'
// import store from "@/store";
import { useStore } from "vuex";
// import { mapMutations } from 'Vuex'
    const store = useStore()
    const form=reactive({
        user: "",
        pwd: "",
      })

     const rules=reactive({
        username: [{ required: true, trigger: "blur", message: "请输入" }],
        password: [{ required: true, trigger: "blur", message: "请输入" }],
      })
  
      //  ...mapMutations("tab", ["setMenu"]),
 
    function submit(){
      // const token = Mock.Random.guid();
      // Cookie.set("token", token);
      // router.push('/home')

      getMenu(form).then(({data})=>{
        console.log(data);
        if(data.code==200){
          console.log(data.data.token);
              Cookie.set("token", data.data.token);
              store.commit('tab/setMenu',data.data.menu)
              router.push('/home')
          }
          else if(data.code===999){
            ElMessage.error('用户名或密码错误')
          }
      })
    }

</script>

<style lang="less" scoped>
.login-container {
  width: 350px;
  margin: 180px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid #7a6868;
  border-radius: 20px;
  padding: 35px 35px 15px 35px;
  background-color: #fff;
  box-shadow: 0 0 25px #cac6c6;
  box-sizing: border-box;

  .login_title {
    margin-bottom: 40px;
  }

  input {
    width: 198px;
  }

  h3 {
    color: rgb(1, 141, 255);
  }
}
</style>
