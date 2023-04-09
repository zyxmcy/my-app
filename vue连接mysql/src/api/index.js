const express = require('express')
const router = express.Router()

const mysql = require('mysql')
let models = require('../server/db')

const conn = mysql.createConnection(models.mysql)
conn.connect()
const jsonW = function (res,ret) {
  console.log('ret:',ret==='undefined', ret===[],typeof ret,ret);
  if(ret.length === 0){
    console.log('登陆失败');
    res.json({
      code:'1',msg:'操作失败'
    })
  }
  else{
    console.log('登陆成功');
    res.json(
      ret
    )
  }
}
// home
router.get('/abc/mysql/all',(req,res)=>{
  const sql = `SELECT * FROM admin`
    conn.query(sql,function(err, result){
      if(err){
        console.log(err)
        console.log('登陆失败');
      }
      if(result){
        console.log('ret:',result);
        jsonW(res,result)
      }
    })
})


module.exports = router