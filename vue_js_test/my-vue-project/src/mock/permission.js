import Mock from "mockjs";
export default {
  getMenu: (x) => {
    const data = [];
    for (let i = 0; i < 50; i++) {
      const work = [];
      for (let j = 0; j < 50; j++) {
        const work_item = {
          salary: Mock.Random.integer(4500, 9000),
          email: Mock.Random.email(),
          address: Mock.Random.county(),
          shop_name: Mock.mock({
            items: {
              id: "@id()",
              name: "@ctitle(10, 15)", // 名称
              description: "@ctitle(12, 20)", // 描述
              picture: "@image(200 * 200)", // 图片
              collectType: "@integer(1, 3)", // 收藏类型，1为商品，2为专题，3为品牌
              price: "@float(60, 1000, 2, 2)", // 商品价格
              discount: "@float(1, 1, 1, 2)", // 折扣信息
              productionPlace: "@province()", // 品牌-产地，多字段通过/分割
              detailsUrl: "@url()", // 详情链接
            },
          }),
        };
        work.push(work_item);
      }
      const item = {
        id: i,
        name: Mock.Random.name(),
        age: Mock.Random.integer(20, 60),
        image: Mock.Random.image(),
        boolean: Mock.Random.boolean(),
        capitalize: Mock.Random.capitalize(),
        cfirst: Mock.Random.cfirst(),
        character: Mock.Random.character(),
        city: Mock.Random.city(),
        clast: Mock.Random.clast(),
        cname: Mock.Random.cname(),
        color: Mock.Random.color(),
        county: Mock.Random.county(),
        cparagraph: Mock.Random.cparagraph(),
        csentence: Mock.Random.csentence(),
        datetime: Mock.Random.datetime(),
        work: work,
      };
      data.push(item);
    }
    return {
      code: 200,
      msg: "success",
      data: data,
    };
  },
};
