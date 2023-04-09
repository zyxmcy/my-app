<template >
  <div class="bj">  </div>
    <el-form label-width="70px" class="login-container" :model="form" :rules="rules">
    <h3 class="login_title">用户登录</h3>
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

import Cookie from "js-cookie";
import { reactive } from "vue";
import router from "@/router";
import {getMenu} from '../api/module/first'
import { ElMessage } from 'element-plus'

import { useStore } from "vuex";

    const store = useStore()
    const form=reactive({
        user: "",
        pwd: "",
      })

     const rules=reactive({
        username: [{ required: true, trigger: "blur", message: "请输入" }],
        password: [{ required: true, trigger: "blur", message: "请输入" }],
      })
  

    function submit(){
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
.bj{
  float: left;
  width: 100%;
  height: 600px;
  background-image: url(https://file.xiazaii.com/file/img/20201016/1yemlph5jub.jpg);
}
.login-container {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 999;
  width: 400px;   
  display: flex;
  margin: 180px auto;
  float: right;
  flex-direction: column;
  background-color: rgb(188, 221, 229);
  align-items: center;
  border: 1px solid #7a6868;
  border-radius: 20px;
  padding: 35px 35px 15px 35px;
  box-shadow: 0 0 25px #eccaca;
  box-sizing: border-box;

  .login_title {
    margin-bottom: 40px;
  }

  input {
    width: 198px;
  }

  h3 {
    color: rgb(9, 204, 97);
  }
}
</style>
