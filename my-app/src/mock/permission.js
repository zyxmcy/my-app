import Mock from 'mockjs'
export default {
    getMenu:config =>{
        const { user, pwd } = JSON.parse(config.body)
        if(user==='admin' && pwd==='123'){
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
                            path: "/mall",
                            name: "mall",
                            label: "商品管理",
                            icon: 'VideoPlay',
                            url: "MallManage/MallManage",
                          },
                          {
                            path: "/user",
                            name: "user",
                            label: "用户管理",
                            icon: 'Avatar',
                            url: "UserManage/UserManage",
                          },
                          {
                            label: "其他",
                            icon: 'Location',
                            children: [
                              {
                                path: "/pageOne",
                                name: "pageOne",
                                label: "页1",
                                icon: "setting",
                                url: "Other/PageOne",
                              },
                              {
                                path: "/PageTwo",
                                name: "pageTwo",
                                label: "页2",
                                icon: "setting",
                                url: "Other/PageTwo",
                              },
                            ],
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
                            path: "/mall",
                            name: "mall",
                            label: "商品管理",
                            icon: 'VideoPlay',
                            url: "MallManage/MallManage",
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