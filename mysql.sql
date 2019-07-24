-- 创建数据库和用户并授权
create database SLF_DB;
create USER 'slf'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
--ALTER USER 'slf'@'%' IDENTIFIED WITH mysql_native_password BY 'password';

GRANT ALL PRIVILEGES ON SLF_DB.* TO slf;
flush privileges

-- 每期中奖信息表（数据源）
CREATE TABLE `TBL_Lottery_Raw_Data` (
  `trem_No` varchar(100) NOT NULL,
  `red_Num` varchar(100) NOT NULL,
  `blue_Num` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`trem_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

-- 中奖信息分析表
-- 可以拓展出更多的分析数据，号码从小到大
CREATE TABLE `TBL_Lottery_analysed_Data` (
  `trem_No` varchar(100) NOT NULL,
  `blue_No1` varchar(100) NOT NULL,
  `blue_No2` varchar(100) NOT NULL,
  `blue_No3` varchar(100) NOT NULL,
  `blue_No4` varchar(100) NOT NULL,
  `blue_No5` varchar(100) NOT NULL,
  `red_No1` varchar(100) NOT NULL,
  `red_No2` varchar(100) NOT NULL,
  PRIMARY KEY (`trem_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

-- 号码池表
-- 所有出现的组合，根据大小进行排序
CREATE TABLE `TBL_Lottery_Number_pool` (
  `blue_No1` varchar(100) NOT NULL,
  `blue_No2` varchar(100) NOT NULL,
  `blue_No3` varchar(100) NOT NULL,
  `blue_No4` varchar(100) NOT NULL,
  `blue_No5` varchar(100) NOT NULL,
  `red_No1` varchar(100) NOT NULL,
  `red_No2` varchar(100) NOT NULL,
  PRIMARY KEY (`blue_No1`,`blue_No2`,`blue_No3`,`blue_No4`,`blue_No5`,`red_No1`,`red_No2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

-- 号码预测信息表
CREATE TABLE `TBL_Lottery_Forcast_Data` (
  `id` bigint(20) NOT NULL auto_increment,
  `trem_No` varchar(100) NOT NULL,
  `blue_No1` varchar(100) NOT NULL,
  `blue_No2` varchar(100) NOT NULL,
  `blue_No3` varchar(100) NOT NULL,
  `blue_No4` varchar(100) NOT NULL,
  `blue_No5` varchar(100) NOT NULL,
  `red_No1` varchar(100) NOT NULL,
  `red_No2` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
