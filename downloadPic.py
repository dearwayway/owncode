#encoding=utf8
#Function: Batch mode for downloading images
#Author: Weiwei Xue
#Create Date: 2015-12-20
#Mofify Date: 2015-12-20

import urllib
import urllib2
import os
import sys

def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False

picNum=sys.argv[2]
folderName=sys.argv[1]
save_path="/Users/Weiwei/Desktop/"+folderName
mkdir(save_path)

for i in range(1,int(picNum)):
	picurl="http://gqzzwr.duapp.com/img.php?name=cyzo201511&page="+str(i).zfill(3)
	imgData = urllib2.urlopen(picurl).read()
	# 给定图片存放名称
	fileName = save_path + "/"+str(i).zfill(3)+".jpg"
	# 文件名是否存在
	#if os.path.exists(fileName):
	output = open(fileName,'wb+')
	output.write(imgData)
	output.close()
	print "Finished download \n"
	print "运行完成"



