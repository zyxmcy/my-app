import Mock from 'mockjs'
export default {
    getMenu:config =>{
        const { user, pwd } = JSON.parse(config.body)
        if(user==='root' && pwd==='123123'){
            return{
                code:200,
                data:{
                   
                        menu: [
                          {
                            path: "/",
                            name: "home",
                            label: "首页",
                            icon: 'House',
                            url: "Home/Home",
                          },
                          {
                            path: "/zodiac",
                            name: "zodiac",
                            label: "十二生肖",
                            icon: 'Picture',
                            url: "ZodiacManage/ZodiacManage",
                          },
                          {
                            path: "/user",
                            name: "user",
                            label: "人物和故事",
                            icon: 'Avatar',
                            url: "UserManage/UserManage",
                          },
                         
                        ],
                    
                    token:Mock.Random.guid(),
                    message:'获取成功'
                }
            }
        }else if(user==='zxc' && pwd==='123'){
            return{
                code:200,
                data:{
                    menu:[
                        
                        {
                            path: "/",
                            name: "home",
                            label: "首页",
                            icon: 'House',
                            url: "Home/Home",
                          },
                          {
                            path: "/zodiac",
                            name: "zodiac",
                            label: "十二生肖",
                            icon: 'VideoPlay',
                            url: "ZodiacManage/ZodiacManage",
                          },
                    ],
                    token:Mock.Random.guid(),
                    message:'获取成功'
                }
            }
        }else{
            return{
                code:999,
                data:{
                    message:'错误'
                }
            }
        }
    }
}