import Mock from 'mockjs'
import permission from './permission'

Mock.mock(/api\/permission\/getMenu/,'post',permission.getMenu)