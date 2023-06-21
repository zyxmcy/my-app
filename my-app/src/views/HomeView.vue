<template>
  <div class="home">
    <el-row>
      <el-col :span="8"
        ><div class="grid-content bg-purple">
          <div class="top">
            <div class="t-context">
              <img src="../images/1.jpg" alt="" />
              <div class="userinfo">
                <p class="name">Admin</p>
                <p class="access">超级管理员</p>
              </div>
            </div>
            <div class="b-context">
              <p>上次登录时间<span>2022-11-31</span></p>
              <p>上次登录地点<span>郑州</span></p>
            </div>
          </div>
          <div class="bottom">
            <el-table :data="tableData" stripe>
              <el-table-column
                v-for="(val, key) in tableList"
                :key="val"
                :prop="key"
                :label="val"
              />
              <!-- <el-table-column prop="date" label="今日卖出" />
              <el-table-column prop="address" label="本月卖出" />
              <el-table-column prop="total" label="总卖出" /> -->
            </el-table>
          </div>
        </div>
      </el-col>

      <el-col :span="16">
        <div class="num">
          <el-card
            body-style="{display: 'flex'}"
            v-for="i in countData"
            :key="i.name"
          >
            <el-icon><component :is="i.icon"></component></el-icon>
            <div>
              <p class="value">{{ i.value }}</p>
              <p class="mz">{{ i.name }}</p>
            </div>
          </el-card>
        </div>
        <el-card style="height: 280px">
          <div class="line"></div>
        </el-card>
        <div class="graph">
          <el-card style="height: 260px"></el-card>
          <el-card style="height: 260px"></el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import * as echarts from "echarts";
import { Check } from "@element-plus/icons-vue";
import { markRaw } from "@vue/reactivity";
import { getdata } from "../api/module/first";
export default {
  name: "HomeView",
  components: { Check },
  data() {
    return {
      tableData: [
        {
          date: "111",
          name: "oppo",
          address: "500",
          total: "10000",
        },
        {
          date: "1111",
          name: "vivo",
          address: "444",
          total: "10000",
        },
        {
          date: "288",
          name: "xiaomi",
          address: "4563",
          total: "10000",
        },
        {
          date: "234",
          name: "meizu",
          address: "233",
          total: "10000",
        },
      ],
      tableList: {
        name: "名字",
        date: "今日卖出",
        address: "本月卖出",
        total: "总卖出",
      },
      countData: [
        {
          name: "今日支付订单",
          value: 1234,
          icon: markRaw(Check),
          color: "#2ec7c9",
        },
        {
          name: "今日支付订单",
          value: 1234,
          icon: markRaw(Check),
          color: "#2ec7c9",
        },
        {
          name: "今日支付订单",
          value: 1234,
          icon: markRaw(Check),
          color: "#2ec7c9",
        },
        {
          name: "今日支付订单",
          value: 1234,
          icon: markRaw(Check),
          color: "#2ec7c9",
        },
        {
          name: "今日支付订单",
          value: 1234,
          icon: markRaw(Check),
          color: "#2ec7c9",
        },
        {
          name: "今日支付订单",
          value: 1234,
          icon: markRaw(Check),
          color: "#2ec7c9",
        },
      ],
      a: 0,
      b: 0,
      c: 0,
      d: 0,
      list: [],
    };
  },
  methods: {
    renwuthree() {
      getdata().then(({ data }) => {
        for (let i = 0; i < data.data.length; i++) {
          const e = data.data[i];
          if (e.year == 2019) {
            this.a++;
          } else if (e.year == 2020) {
            this.b++;
          } else if (e.year == 2021) {
            this.c++;
          } else if (e.year == 2022) {
            this.d++;
          }
        }
        this.list = [this.a, this.b, this.c, this.d];
        // console.log(this.list);
      });
    },
    echart() {
      var myEcharts = echarts.init(document.querySelector(".line"));
      var option = {
        xAxis: { data: ["2019", "2020", "2021", "2022"] },
        yAxis: {
          type: "value",
        },
        series: [
          {
            type: "line",
            data: this.list,
          },
        ],
      };
      myEcharts.setOption(option);
    },
  },
  // mounted() {
  //   this.renwuthree();
  //   // console.log(this.list);
  //   setTimeout(() => {
  //     console.log(this.list);
  //     this.echart();
  //   }, 5000);
  // },
};
</script>


<style lang="less">
.home {
  padding: 0px;
}
.line {
  width: 100%;
  height: 250px;
}
.bg-purple {
  border: 1px solid #efefef;
  .top {
    .t-context {
      display: flex;
      justify-content: center;
      align-items: center;
      padding-bottom: 20px;
      padding-top: 20px;
      border-bottom: 1px solid #efefef;
      img {
        margin-right: 2.5rem;
        width: 9.375rem;
        height: 9.375rem;
        border-radius: 50%;
      }
      .userinfo {
        margin-top: 10px;
        .name {
          font-size: 32px;
          margin-bottom: 10px;
        }
        .access {
          color: #836f6f;
        }
      }
    }
    .b-context {
      padding-top: 10px;
      color: #999;
      font-size: 16px;
      line-height: 28px;
      p {
        span {
          color: #666;
          margin-left: 60px;
        }
      }
    }
  }
  .el-table--fit {
    margin-top: 40px;
  }
}
.num {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  .value {
    font-size: 30px;
    margin-bottom: 10px;
    line-height: 30px;
    height: 30px;
  }
  .mz {
    font-size: 10px;
    color: #999;
    text-align: center;
  }
  // display: flex;

  .el-card__body {
    display: flex;
  }
  .el-card {
    width: 32%;
    margin-bottom: 20px;
  }

  i {
    width: 80px;
    height: 80px;
    font-size: 30px;
    text-align: center;
    color: white;
    background-color: blue;
    margin-right: 20px;
  }
}
.graph {
  display: flex;
  justify-content: space-between;
  .el-card {
    width: 48%;
  }
}
</style>