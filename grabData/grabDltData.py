"""
福建体彩大乐透 期数查询 请求地址
http://www.lottery.gov.cn/historykj/history_91.jspx?page=false&_ltype=dlt&termNum=0&startTerm=07001&endTerm=07008
"""
# -*- coding: gbk -*-
import http.client
import http.client
import requests
import socket
import time
import random

from bs4 import BeautifulSoup

# 根据期数获取大乐透的数据信息
def getLotteryDataByNo(minNo,maxNo):
    timeout = random.choice(range(80, 180))
    url = "http://www.lottery.gov.cn/historykj/history_91.jspx?page=false&_ltype=dlt&termNum=0&startTerm="+minNo+"&endTerm="+maxNo
    while True:
        try:
            rep = requests.get(url)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))

    return wrapData(rep.text)

def wrapData(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body  # 获取body部分
    mainTable = body.find('div', {'class': 'result'})  # 找到主表信息（内含大乐透数据）
    tremList = mainTable.select('tbody tr') # 获取期数数据

    for tremSource in tremList:  # 对每期中的数据进行分析
        temp = []
        tremNo = tremSource.select('td')[0].string
        temp.append(tremNo)

        redNumberSource = tremSource.select('td[class="red"]')  # 找到找到前区号码
        blueNumberSource = tremSource.select('td[class="blue"]')  # 找到找到后区号码

        redNumbers = ""
        for redNumber in redNumberSource:
            # 拼接普号数据
            redNumbers += redNumber.string+","
        temp.append(redNumbers)

        blueNumbers= ""
        for blueNumber in blueNumberSource:
            blueNumbers += blueNumber.string+","
        temp.append(blueNumbers)
        final.append(temp)
    return final

