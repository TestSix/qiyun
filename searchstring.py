#coding=utf-8

import sys
import linecache
# 读去传入的参数 文件名 查找字符（未作校验）
logname=sys.argv[1]
strname=sys.argv[2]
nw=0

#读取文件，每行作为列表的形式
filelist = linecache.getlines(logname)
for list in filelist:
	#查找字符串 如果判断如果不存在返回负一
	if list.find(strname)!=-1:
		#去掉换行符
		lis= list.strip('\n')
		nw=1
		print lis
if nw=0：
	print '查找的字符不存在'
#未判断传入的 文件名  字符串 是否符合规范   
