import Cookie from 'js-cookie'
export default {
    namespaced:true,
    state:{
            isCollaps:false,
            tabsList:[
                {
                path: "/",
                name: "home",
                label: "首页",
                icon: 'House',
                url: "Home/Home",
              }
            ],
            menu:[] 
        },
    mutations:{
        // 修改菜单展开收起
        chengrCollaps(state){
            state.isCollaps=!state.isCollaps
            console.log(state.isCollaps);
        },
        // 
        selectMenu(state,item){
            if(item.name!=='home'){
                const index = state.tabsList.findIndex(x=>x.name === item.name)
                if(index==-1){
                    console.log(item);
                    state.tabsList.push(item)
                }
            }
        },
        //删除指定的tag数据
        closetag(state,item){
            console.log(item);
            const index = state.tabsList.findIndex(x=>x.name===item.name)
            state.tabsList.splice(index,1)
        },
        // 设置menu的数据
        setMenu(state,val){
                state.menu=val
                Cookie.set('menu',JSON.stringify(val))
        }
    }
}