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

def getLastestTermNo():
    url = "http://www.lottery.gov.cn/historykj/history.jspx?page=false&_ltype=dlt&termNum=1"
    return wrap_data(geturlcontent(url))

# 根据期数获取大乐透的数据信息
def getLotteryDataByNo(minNo,maxNo):
   url = "http://www.lottery.gov.cn/historykj/history_91.jspx?page=false&_ltype=dlt&termNum=0&startTerm={0}&endTerm={1}".format(
       minNo, maxNo)
   return wrap_data(geturlcontent(url))


def geturlcontent(url):
    # timeout = random.choice(range(80, 180))
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
    return rep.text

def wrap_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body  # 获取body部分
    main_table = body.find('div', {'class': 'result'})  # 找到主表信息（内含大乐透数据）
    trem_list = main_table.select('tbody tr') # 获取期数数据

    for tremSource in trem_list:  # 对每期中的数据进行分析
        temp = []
        trem_no = tremSource.select('td')[0].string
        temp.append(trem_no)

        red_number_source = tremSource.select('td[class="red"]')  # 找到找到前区号码
        blue_number_source = tremSource.select('td[class="blue"]')  # 找到找到后区号码

        red_numbers = ""
        for redNumber in red_number_source:
            # 拼接普号数据
            red_numbers += redNumber.string+","
        temp.append(red_numbers)

        blue_numbers = ""
        for blueNumber in blue_number_source:
            blue_numbers += blueNumber.string+","
        temp.append(blue_numbers)
        final.append(temp)
    return final



