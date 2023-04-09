// node 后端服务器
const api = require('./index')
const cors = require('cors')
const express = require('express')
const app = express()

app.use(cors())

app.all("*", function(req, res, next) {

    res.header("Access-Control-Allow-Origin", "*");
 
    res.header("Access-Control-Allow-Headers", "content-type");
  
    res.header("Access-Control-Allow-Methods", "DELETE,PUT,POST,GET,OPTIONS");
    if (req.method.toLowerCase() == 'options')
      res.send(200); 
    else
      next();
  })


app.use('/ap/Stu', api)
// 监听端口
app.listen(5000)
console.log('success listen at port:5000......')