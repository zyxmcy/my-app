// import http from '../http'
import get from '../http'
import permission from '../../mock/index'
import axios from 'axios'
// export const getdata = ()=> http.post('/selectGoodsInfo',{})
export const getdata = ()=> get()

export const getMenu =(data)=>axios.post('/api/permission/getMenu',data)