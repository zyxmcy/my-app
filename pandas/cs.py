from pyecharts import options as opts
from pyecharts.charts import Calendar
from pyecharts.charts import Pie
import pandas as pd
import numpy as np
from save_results_B import *

# 1、数据处理

1.1：读取数据

读取`Consumption.csv`、`attendance.csv`、`teacher.csv`、`mark.csv`四个表的数据，分别保存到变量`data_Consumption`、`data_attendance`、`data_teacher`、`data_mark`。并运行给出的答案保存代码保存答案。

表所在路径如下：

`Consumption.csv`路径：'./data/Consumption.csv'

`attendance.csv`路径：'./data/attendance.csv'

`teacher.csv`路径：'./data/teacher.csv'

`mark.csv`路径：'./data/mark.csv'

例如：变量名 = pd.read_csv('路径')

# TODO：

data_Consumption = pd.read_csv("./data/Consumption.csv")
data_attendance = pd.read_csv("./data/attendance.csv")
data_teacher = pd.read_csv("./data/teacher.csv")
data_mark = pd.read_csv("./data/mark.csv")

save_task1_1(data_Consumption, data_attendance, data_teacher, data_mark)

1.2 分析变量`data_Consumption`，将`DealTime`列处理为日期格式，将处理的结果更新到变量`data_Consumption`，并运行给出的答案代码保存答案。

> 日期格式: datetime64[ns]

# TODO：
data_Consumption["DealTime"] = pd.to_datetime(data_Consumption["DealTime"])

save_task1_2(data_Consumption)

1.3 分析变量`data_Consumption`，将`MonDeal`转为正数，将处理的结果更新到变量`data_Consumption`，并运行给出的答案代码保存答案。

# TODO：
data_Consumption["MonDeal"] = data_Consumption["MonDeal"].abs()

save_task1_3(data_Consumption)

1.4 分析变量`data_attendance`，处理2014年2月份的数据，将`qj_term`更新为'2013-2014-2'，将处理后的结果更新到变量`data_attendance`，并运行给出的答案代码保存答案。

# TODO:
data_attendance["DataDateTime"] = pd.to_datetime(
    data_attendance["DataDateTime"])
data_attendance["DataDateTime"]
zz = (data_attendance["DataDateTime"].dt.year == 2014) & (
    data_attendance["DataDateTime"].dt.month == 2)
data_attendance.loc[zz, "qj_term"] = "2013-2014-2"
data_attendance[zz]

save_task1_4(data_attendance)

# 2、校园教师信息分析

print(data_teacher[["sub_Name", "bas_id"]])
print(data_teacher[["sub_Name", "bas_id"]].drop_duplicates())

2.1 分析变量`data_teacher`中的`sub_Name`、`bas_id`两列数据，统计各个学科的老师数量，返回拥有老师最多的学科名，结果保存到变量`task2_1`中，并运行给出的答案保存代码保存答案。

# TODO:
print(data_teacher.groupby("sub_Name").bas_id.nunique())
print(data_teacher[["sub_Name", "bas_id"]].drop_duplicates().groupby(
    "sub_Name").bas_id.count())
print(data_teacher.drop_duplicates(
    subset=["sub_Name", "bas_id"]).groupby("sub_Name").bas_id.count())
task2_1 = data_teacher.drop_duplicates(
    subset=["sub_Name", "bas_id"]).groupby("sub_Name").bas_id.count().idxmax()
task2_1

save_task2_1(task2_1)

2.2 分析变量`data_teacher`中的`term`、`gra_Name`、`bas_id`3列数据，观察"2014-2015-1"学期老师的教学情况，统计有多少老师涉及多个年级的课程，结果保存到变量`task2_2`中，并运行给出的答案保存代码保存答案。

# TODO:
zz = data_teacher[data_teacher["term"] == "2014-2015-1"]
print((zz.groupby("bas_id").gra_Name.nunique() > 1).sum())
print((zz.drop_duplicates(subset=["gra_Name", "bas_id"]).groupby(
    "bas_id").gra_Name.count() > 1).sum())
print((zz[["gra_Name", "bas_id"]].drop_duplicates().groupby(
    "bas_id").gra_Name.count() > 1).sum())
task2_2 = 10
print((zz.drop_duplicates(["gra_Name", "bas_id"]
                          ).bas_id.value_counts() > 1).sum())

save_task2_2(task2_2)

2.3 分析变量`data_teacher`中的`term`、`cla_Name`、`bas_id`3列数据，观察"2014-2015-1、2014-2015-2"两学期老师的教学情况，统计每位老师授课班级数量，返回上课班级最多的`bas_id`，结果保存到变量`task2_3`中，并运行给出的答案保存代码保存答案。

# TODO:
xx = data_teacher[(data_teacher["term"] == "2014-2015-1") |
                  (data_teacher["term"] == "2014-2015-2")]
task2_3 = xx.drop_duplicates(["cla_Name", "bas_id"]).groupby(
    "bas_id").cla_id.count().idxmax()

save_task2_3(task2_3)

data_teacher

2.4 分析变量`data_teacher`中的`term`、`cla_Name`、`gra_Name`3列数据，统计每学期各年级班级的数量，返回班级最多的学期和年级，结果保存到变量`task2_4`，并运行给出的答案保存代码保存答案。
* 保存格式：(学期, 年级)

# TODO:
print(data_teacher.drop_duplicates(["term", "cla_Name"]).groupby(
    ["term", "gra_Name"]).cla_id.count().idxmax())
print(data_teacher.groupby(["term", "gra_Name"]).cla_id.nunique().idxmax())
task2_4 = ('2018-2019-1', '高一')

save_task2_4(task2_4)

2.5 分析变量`data_teacher`, 统计'2014-2015-1'学期，高三物理学科和地理学科各开设了多少个班，结果保存到变量`task2_5`，并运行给出的答案保存代码保存答案。
* 保存格式: (开设地理课的班级数量, 开设物理课的班级数量)

# TODO:
xx = zz[(zz["gra_Name"] == "高三") & (zz["sub_Name"].str.contains("地理|物理"))]
cc = xx.groupby("sub_Name").cla_Name.count()
task2_5 = (cc[0], cc[1])
task2_5
cc

save_task2_5(task2_5)

# 3、校园考勤统计

3.1 分析变量`data_attendance`，统计`controler_name`包含`校服`的考勤有多少条？结果保存到变量`task3_1`，并运行给出的答案保存代码保存答案。

# TODO:
contain_xiaofu = data_attendance[data_attendance["controler_name"].str.contains(
    "校服")]
task3_1 = len(contain_xiaofu)
print(task3_1)
print(contain_xiaofu.count().kaoqing_id)

save_task3_1(task3_1)

3.2 分析变量`data_attendance`，统计高一年级迟到早退次数最多的`bf_studentID`，结果保存到变量`task3_2`，并运行给出的答案保存代码保存答案。
>迟到：`controler_name`包含迟到

>早退：`controler_name`包含早退

# TODO:
vv = data_attendance[(data_attendance["cla_Name"].str.contains("高一")) & (
    data_attendance["controler_name"].str.contains("迟到|早退"))]
task3_2 = vv.groupby("bf_studentID").kaoqing_id.count().idxmax()
task3_2

save_task3_2(task3_2)

3.3 分析变量`data_attendance`，计算考勤次数大于200次的`bf_classid`中，每个班级迟到次数加早退次数占该班级考勤总次数的比例，返回最大的比例，结果保存到变量`task3_3`，并运行给出的答案保存代码保存答案。
> 结果保留三位小数

# TODO:
df = data_attendance.groupby("bf_classid").agg(
    {"kaoqing_id": "count"}).reset_index()
df = df[df["kaoqing_id"] > 200]
# print(df)
res = pd.merge(df, data_attendance, how="left", on="bf_classid")
total_200 = res.groupby("bf_classid").kaoqing_id_x.count()
# print(total_200)
mm = res[res["controler_name"].str.contains("迟到|早退")]
late = mm.groupby("bf_classid").kaoqing_id_x.count()
# print(late)
print((late/total_200).max().round(2))
task3_3 = (late/total_200).max().round(2)
task3_3

save_task3_3(task3_3)

3.4 分析变量`data_attendance`，以小时统计迟到早退的次数，返回迟到早退的高峰期是在一天的哪个时间（24小时制），结果保存到变量`task3_4`，并运行给出的答案保存代码保存答案。

# TODO:
data_attendance["hour"] = data_attendance["DataDateTime"].dt.hour
later = data_attendance[data_attendance["controler_name"].str.contains(
    "迟到|早退")]
# print(later)
task3_4 = later.groupby("hour").kaoqing_id.count().idxmax()
task3_4

save_task3_4(task3_4)

# 4 学生成绩分析

4.1 分析变量`data_mark`，计算`exam_number`为289考试中，高二各班级化学学科的平均分，返回平均分最高的`cla_id`，结果保存到变量`task4_1`，运行结果保存代码保存答案。

# TODO:
exam289 = data_mark[data_mark["exam_number"] == 289]
res = exam289[(exam289["cla_Name"].str.contains("高二")) &
              (exam289["mes_sub_name"].str.contains("化学"))]
task4_1 = res.groupby("cla_id")["mes_Score"].mean().idxmax()
task4_1

save_task4_1(task4_1)

data_mark

4.2 分析变量`data_mark`，将`exam_number`为289考试中化学学科的成绩, 按以下要求对成绩进行划分成绩等级，统计各成绩等级所对应的人数，返回人数分布最多的成绩等级（免考、不及格、及格、中等、良、优），结果保存到变量`task4_2`，运行结果保存代码保存答案。

* 分数 = -3: 免考
* -2 <= 分数 < 60: 不及格
* 60 <= 分数 < 70: 及格
* 70 <= 分数 < 80: 中等
* 80 <= 分数 < 90: 良
* 90 <= 分数 <= 100: 优

# TODO:
bins = [-3, -2, 60, 70, 80, 90, 101]
label = ["免考", "不及格", "及格", "中等", "良", "优"]
data_mark["成绩等级"] = pd.cut(data_mark["mes_Score"],
                           bins=bins, labels=label, right=False)
print(data_mark.groupby("成绩等级").bf_StudentID.count())
task4_2 = data_mark["成绩等级"].value_counts().idxmax()


save_task4_2(task4_2)

4.3 分析变量`data_mark`，以`exam_number`为289考试中化学学科的成绩作为一个组别，计算这组数据的Z_score，求Z_score大于0的有多少个？结果保存到变量`task4_3`，运行结果保存代码保存答案。
* Z_score，是一种具有相等单位的量数。它是将原始分数与团体的平均数之差除以标准差所得的商数，是以标准差为单位度量原始分数离开其平均数的分数之上多少个标准差，或是在平均数之下多少个标准差。

$$
Z\_score = （分数-平均分数）\div标准差
$$

# TODO:
exam289_huaxue = exam289[exam289["mes_sub_name"] == "化学"]
task4_3 = (((exam289_huaxue["mes_Score"]-exam289_huaxue["mes_Score"].mean()
             )/exam289_huaxue["mes_Score"].std()) > 0).sum()
task4_3

save_task4_3(task4_3)

4.4 分析变量`data_mark`，统计`exam_number`为284的考试中各班级作弊和缺考次数，返回作弊加缺考次数最多的`cla_id`，结果保存到变量`task4_4`，运行结果保存代码保存答案。

# TODO:
exam284 = data_mark[data_mark["exam_number"] == 284]
exam284_zb_or_qk = exam284[(exam284["mes_Score"] == -2)
                           | (exam284["mes_Score"] == -1)]
task4_4 = exam284_zb_or_qk.groupby("cla_id").count().mes_Score.idxmax()
task4_4

save_task4_4(task4_4)

# 5 校园消费统计

5.1 分析变量`data_Consumption`，按小时分析，不同时间的消费总金额，消费最多的金额是多少？结果保存到变量`task5_1`，并运行结果保存代码保存答案。
> (保留两位小数)

# TODO:
data_Consumption["hour"] = data_Consumption["DealTime"].dt.hour
task5_1 = data_Consumption.groupby("hour").MonDeal.sum().max()
task5_1

save_task5_1(task5_1)

5.2 分析变量`data_Consumption`，按周一到周七计算日均总消费额，日均总消费额最多的是周几？结果保存到变量`task5_2`，并运行结果保存代码保存答案。
>结果保存为数字。周一到周七分别为1到7

# TODO:
data_Consumption["weekday"] = data_Consumption["DealTime"].dt.weekday+1
data_Consumption["day"] = data_Consumption["DealTime"].dt.date
task5_2 = (data_Consumption.groupby("weekday").MonDeal.sum() /
           data_Consumption.groupby("weekday").day.nunique()).idxmax()
task5_2

save_task5_2(task5_2)

5.3 分析变量`data_Consumption`，计算2018年高一到高三各年级的消费金额，消费总金额最多的年级（高一、高二、高三）是？结果保存到变量`task5_3`，并运行结果保存代码保存答案。

# TODO:
date_2018 = data_Consumption[data_Consumption["DealTime"].dt.year == 2018]
date_2018["年级"] = date_2018["cla_Name"].str.extract("(高一|高二|高三)")
task5_3 = date_2018.groupby("年级").MonDeal.sum().idxmax()
task5_3

save_task5_3(task5_3)

data_Consumption

5.4 分析变量`data_Consumption`，按周分析，计算周一到周七统计日均消费次数，并绘制圆环图。

> 次数保留整数

# TODO:
total = data_Consumption.groupby("weekday").DealTime.count()
timer = data_Consumption.groupby("weekday").day.nunique()
res = (total/timer).round(0)
res
week = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
c = (
    Pie().add(
        "",
        [list(z) for z in zip(week, res.values)],
        radius=["50%", "75%"]
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="消费次数")
    ).set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}:{c}")
    )
)
c.render_notebook()

5.5 分析变量`data_Consumption`，查看2018年11月的消费记录，计算每天的消费总额，并绘制日历图。

* 设置视觉映射配置项范围(0, 60000)
* 日历图设置水平显示

# TODO:
res = data_Consumption[(data_Consumption["DealTime"].dt.year == 2018) & (
    data_Consumption["DealTime"].dt.month == 11)]
data = res.groupby("day").MonDeal.sum()
c = (
    Calendar().add(
        "",
        [list(x) for x in zip(data.index, data.values)],
        calendar_opts=opts.CalendarOpts(range_="2018-11")
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="消费总额"),
        visualmap_opts=opts.VisualMapOpts(max_=60000),
    )
)
c.render_notebook()
