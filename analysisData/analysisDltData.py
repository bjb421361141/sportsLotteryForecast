from persistData import persistData
from utils import DBUtil


# 选码组合数据池的生成（号码池表 TBL_Lottery_Number_pool）
def init_lottery_number_pool():
    # 初始化组合的第一种情况35选5 12选2
    tmp1 = []
    for x in range(0, 35):
        tmp1.append(x + 1)
    permutations35_5 = _permutations_combinations(tmp1, 5)
    persistData.batchSaveLotteryNumberPoolBlue(permutations35_5)

    tmp2 = []
    for x in range(0, 12):
        tmp2.append(x + 1)
    permutations12_2 = _permutations_combinations(tmp2, 2)
    persistData.batchSaveLotteryNumberPoolRed(permutations12_2)
    return None


# 排列组合
# 根据数据源，选择排列个数 来生成所有的排列结果（去重后，按小到大）
def _permutations_combinations(source, permu_nums):
    source_size = len(source)
    if source_size < permu_nums:
        return source
    result = []
    # 初始化组合的第一种情况
    tmp = []
    for x in range(0, source_size):
        tmp.append(0)
    i = 0
    while i < permu_nums:
        tmp[i] = 1
        i = i + 1
    result.append(_transform(source, tmp))
    # 处理第一个外的排列组合情况
    flag = True
    temp_flag = False
    while flag:
        pos = 0
        cout = 0
        # 校验是否可以结束，以所有1右移为结束标志
        for i in range(0, permu_nums):
            if tmp[-1 - i] == 1:
                temp_flag = True
            else:
                temp_flag = False
                break
        if temp_flag:
            flag = False
        else:
            # 首先找到第一个10组合，然后变成01，同时将左边所有的1移动到数组的最左边
            for i, x in enumerate(tmp):
                if i < len(tmp) - 1 and tmp[i] == 1 and tmp[i + 1] == 0:
                    tmp[i] = 0
                    tmp[i + 1] = 1
                    pos = i
                    break
            # 左移所有的1，计算1的个数并重新赋值0到pos的数据
            for i in range(0, pos + 1):
                if tmp[i] == 1:
                    cout = cout + 1
            for i in range(0, pos + 1):
                if i < cout:
                    tmp[i] = 1
                else:
                    tmp[i] = 0
            # 将排列后的数据直接添加
            result.append(_transform(source, tmp))
    return result


def _transform(source, m_code):
    result = []
    for i, x in enumerate(m_code):
        if x == 1:
            result.append(source[i])
    return result


# 往期数据的处理（中奖详情表（分析） TBL_Lottery_analysed_Data ）
def analyse_raw_data():
    conn = DBUtil.getConnection("192.168.245.128", "slf", "slf1234", "SLF_DB")
    sql = "SELECT trem_No,blue_Num,red_Num FROM TBL_Lottery_Raw_Data"
    data = DBUtil.getDataBySQL(sql, conn)
    if len(data) > 0:
        final = []
        for rawData in data:
            tmp = [rawData[0]]
            blue = (rawData[1].strip(",")).split(",")
            red = (rawData[2].strip(",")).split(",")
            if len(blue) == 5 and len(red) == 2:
                blue.sort()
                red.sort()
                tmp += blue
                tmp += red
            # 计算每一组中奖数据的离散情况
            ls_blue = _get_lsval(blue)
            ls_red = _get_lsval(red)
            tmp.append(ls_blue)
            tmp.append(ls_red)
            final.append(tmp)
        if len(final) > 0:
            # 这边对连接进行关闭
            persistData.saveAnalysedData(final)
    return len(final)


def _get_lsval(list):
    max_num = max(list)
    ls_sum = 0
    for x in list:
        if isinstance(x, (str, float, int)):
            # 最大值与各个值差的平方
            ls_sum = ls_sum + pow((int(max_num) - int(x)), 2)
    return ls_sum

# 筛选号码
def select_nums():
    conn = DBUtil.getConnection("192.168.245.128", "slf", "slf1234", "SLF_DB")
    sql = "SELECT ls_blue,ls_red FROM TBL_Lottery_analysed_Data"
    data = DBUtil.getDataBySQL(sql, conn)
    # 分成两组数据分别计算均值和标准差，获取大概率的区间？


