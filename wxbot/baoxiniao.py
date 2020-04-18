#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import pymysql
import json

# 打开数据库连接
db = pymysql.connect("host", "dbuser", "dbpassword", "db")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT count(*) FROM xxx where  TO_DAYS( NOW( ) ) - TO_DAYS( time ) <= 1"
donesql =  "SELECT count(*) cccc,sum(bbb) xxxx FROM xxx where  TO_DAYS( NOW( ) ) - TO_DAYS( time ) <= 1 and order_status=11  "


try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchone()
    newOrderCount = results[0]

    cursor.execute(donesql)
    doneResult = cursor.fetchone()
    doneOrderCount = doneResult[0]
    doneFee = doneResult[1]

    #print(newOrderCount)
    #print(doneOrderCount)
    #print(doneFee)

    report  = "昨天新增订单%s笔;完成订单%s笔;收取手续费%s元！" % (newOrderCount,doneOrderCount,doneFee)
    robotMsg = {
        "msgtype": "text",
        "text" :{"content":report }
    }

   robotMsg2= {
    "msgtype": "markdown",
    "markdown": {
        "content": "平台昨日新增订单<font color=\"warning\">%s</font>\n" \
         " >完成订单:<font color=\"comment\">%s</font>\n" \
         " >收取手续费:<font color=\"comment\">%s</font>\n" \
         " >充值资质金:<font color=\"comment\">数据更新中</font>" % (newOrderCount,doneOrderCount,doneFee)
      }
    }
 
    request = requests.post("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=dfba7b98-7501-4bd7-a532-efb3bb451e9f",json.dumps(robotMsg2))
    print(report)
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()

