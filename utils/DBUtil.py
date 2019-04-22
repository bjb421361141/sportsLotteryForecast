import pymysql

# 根据传入的sql做查询操作
def getConnection(remoteServerIp,userId,passwd,dbNm):
    # db = pymysql.connect("192.168.245.168", "root", "12345678", "mysql")
    db = pymysql.connect(remoteServerIp, userId, passwd, dbNm)
    return db

# 根据传入的sql做数据更新操作
def closeConnection(conn):
    conn.close()

# 根据传入的sql做查询操作
def getDataBySQL(sql, conn):
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

# 根据传入的sql做数据更新操作
def saveData(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
