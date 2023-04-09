import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import main from '../views/main.vue'
import Zodiac from '../views/Zodiac.vue'
import Login from '../views/Login'
import Cookie from 'js-cookie'
const routes = [
  {
    path:'/',
    component:main,
    redirect:'/home',
    children:[
      {
        path: '/home',
        name: 'home',
        component: HomeView
      },
      {
        path: '/zodiac',
        name: 'zodiac',
        component: Zodiac
      },
      {
        path: '/User',
        name: 'user',
        component: () => import(/* webpackChunkName: "about" */ '../views/User.vue')
      }
    ]
  },
  {
    path:'/login',
    name:'login',
    component:Login
  }
  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to,from,next)=>{
  const token = Cookie.get('token')
  if(!token && to.name!=='login'){
      next ({name:'login'})
  }else if(token&&to.name==='login'){
      next({name:from.home})
  }else{
      next()
  }
})

export default router
