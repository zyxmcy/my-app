import ws from 'ws';
const wss = new ws.Server({ port: 8080}, ()=>{
    console.log('socker服务启动成功');
    
})

const state = {
    HEART:1,
    MESSAGE:2
}

wss.on('connection',(socket)=>{
    console.log('客户连接成功');
    socket.on('message',(e)=>{
        console.log(e.toString());
        wss.clients.forEach((client)=>{
            client.send(JSON.stringify({
                type:state.MESSAGE,
                message:e.toString()
            }))
        })
    })

     //   socket 长时间不使用 网络波动 弱网模式 他是有可能会断开的
    // 心跳检测 进行保活 保持连接
    
    const heartCheck = ()=>{
        if (socket.readyState === ws.OPEN) {
            socket.send(JSON.stringify({
                type: state.HEART,
                message: "心跳检测"
            }))
        }else{
            clearInterval(heartInreaval)
        }
    }
    let heartInreaval = setInterval(heartCheck,5000)
})

   