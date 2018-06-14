#coding=utf-8
import requests
import pymysql
def getAccessToken():
    url1 = 'http://pos.weipass.cn/weipossoa/accessToken/get?consumerAppCode=100254&secret=vdxunvjb&providerAppCode=100235'
    res= requests.get(url=url1).json()
    accessToken=res['data']['accessToken']
    #print(res)
    #print(res['data']['accessToken'])
    print(accessToken)

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "admin", "accesstoken")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql="update accesstoken set accesstoken = '%s'" % (accessToken)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        print("Error")
        db.rollback()

    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    getAccessToken()
