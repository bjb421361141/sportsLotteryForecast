
# 保存每期中奖号码信息
from utils import DBUtil

# 保存中奖源数据
def saveDltData(dltdatas):

    conn = DBUtil.getConnection("192.168.245.128", "slf", "slf1234", "SLF_DB")
    for row in dltdatas:
        sql = '''INSERT INTO TBL_Lottery_Raw_Data(trem_No,blue_Num,red_num) VALUES('{0}','{1}','{2}')'''.format(*row)
        DBUtil.saveData(sql, conn)
    conn.commit()
    DBUtil.closeConnection(conn)

# 保存分析后的数据 TBL_Lottery_analysed_Data
def saveAnalysedData(analyseDatas):

    conn = DBUtil.getConnection("192.168.245.128", "slf", "slf1234", "SLF_DB")
    for row in analyseDatas:
        sql = '''INSERT INTO TBL_Lottery_analysed_Data(trem_No,blue_No1,blue_No2,blue_No3,blue_No4,blue_No5,red_No1, red_No2,ls_blue,ls_red) 
                VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')'''.format(*row)
        DBUtil.saveData(sql, conn)
    conn.commit()
    DBUtil.closeConnection(conn)

# 保存蓝色号码
def batchSaveLotteryNumberPoolBlue(blue_nums_list):
    # 根据两个参数进行全连接进行数据的保存
    conn = DBUtil.getConnection("192.168.245.128", "slf", "slf1234", "SLF_DB")
    # 循环保存所有可能的组合
    for x in blue_nums_list:
        sql = '''insert into TBL_Lottery_Number_pool_blue(blue_No1,blue_No2,blue_No3,blue_No4,blue_No5) 
                                      VALUES  ('{0}','{1}','{2}','{3}','{4}') '''.format(*x)
        DBUtil.saveData(sql, conn)
    conn.commit()
    DBUtil.closeConnection(conn)
    return None

# 保存红色号码
def batchSaveLotteryNumberPoolRed(red_nums_list):
    # 根据两个参数进行全连接进行数据的保存
    conn = DBUtil.getConnection("192.168.245.128", "slf", "slf1234", "SLF_DB")
    # 循环保存所有可能的组合
    for x in red_nums_list:
        sql = '''insert into TBL_Lottery_Number_pool_red(red_No1,red_No2) 
                                      VALUES  ('{0}','{1}') '''.format(*x)
        DBUtil.saveData(sql, conn)
    conn.commit()
    DBUtil.closeConnection(conn)
    return None
