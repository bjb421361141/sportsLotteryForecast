import csv

from analysisData import analysisDltData
from grabData import grabDltData
from utils import DBUtil
from persistData import persistData

"""写入文件csv： 
将数据抓取出来后我们要将他们写入文件，具体代码如下："""


def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


# 主函数：
# 目标：
if __name__ == '__main__':
    # 1、 初始化号码数据池
    # analysisDltData.init_lottery_number_pool()
    # 2、抓取中奖情况数据
    # result = grabDltData.getLotteryDataByNo("07001","19055")
    # persistData.saveDltData(result)
    # write_data(result, 'C:\\Users\\Baijb\\Desktop\\lottery.csv') # 后续考虑使用Mysql进行数据存储

    # 3、分析中奖数据
    # analysisDltData.analyse_raw_data()

    # 4、数据预测 计算均值和平方差 μ为均数，σ为标准差
    # 使用正态分布计算大概率的区间
    # 计算所有组合的离散值，把符合区间中的组合选出，


