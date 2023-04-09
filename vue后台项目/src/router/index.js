import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import main from '../views/main.vue'
import mall from '../views/Mall.vue'
import PageTwo from '../views/PageTwo.vue'
import PageOne from '../views/PageOne.vue'
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
        path: '/mall',
        name: 'mall',
        component: mall
      },
      {
        path: '/PageTwo',
        name: 'pageTwo',
        component: PageTwo
      },
      {
        path: '/PageOne',
        name: 'pageOne',
        component: PageOne
      },
      {
        path: '/User',
        name: 'user',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
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
  // console.log(token);
  if(!token && to.name!=='login'){
    // console.log('!token');
      next ({name:'login'})
  }else if(token&&to.name==='login'){
    // console.log('token');
      next({name:from.home})
  }else{
    // console.log('next');
      next()
  }
})

export default router
