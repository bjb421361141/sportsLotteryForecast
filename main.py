import csv
from grabData import grabDltData

"""写入文件csv： 
将数据抓取出来后我们要将他们写入文件，具体代码如下："""


def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


# 主函数：
if __name__ == '__main__':
    result = grabDltData.getLotteryDataByNo("07001","07008")
    write_data(result, 'C:\\Users\\Baijb\\Desktop\\lottery.csv') # 后续考虑使用MongoDB进行数据存储
