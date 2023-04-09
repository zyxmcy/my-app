import Mock from 'mockjs'
import mock from './mock'

Mock.mock(/api\/mock\/getMenu/,'post',mock.getMenu)