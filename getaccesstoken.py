import requests
import pymysql
def getAccessToken():
    url1 = 'http://pos.weipass.cn/weipossoa/accessToken/get?consumerAppCode=100254&secret=vdxunvjb&providerAppCode=100235'
    res= requests.get(url=url1).json()
    accessToken=res['data']['accessToken']
    #print(res)
    #print(res['data']['accessToken'])
    print(accessToken)

    # �����ݿ�����
    db = pymysql.connect("localhost", "root", "admin", "accesstoken")
    # ʹ��cursor()������ȡ�����α�
    cursor = db.cursor()
    # SQL �������
    sql="update accesstoken set accesstoken = '%s'" % (accessToken)

    try:
        # ִ��SQL���
        cursor.execute(sql)
        # �ύ�����ݿ�ִ��
        db.commit()
    except:
        # ��������ʱ�ع�
        print("Error")
        db.rollback()

    # �ر����ݿ�����
    db.close()

if __name__ == '__main__':
    getAccessToken()