#encoding=utf-8

import random
oldf=open('/Users/Weiwei/Desktop/index.txt','r')  #打开原文件
newf=open('/Users/Weiwei/Desktop/index.result','w') #打开要写入文件
lines=oldf.readlines()    #原文件行列表
#randline=random.randint(0,len(lines))  # 若干行
randline=50
for i in xrange(0,randline):
        newf.write(lines[random.randint(0,len(lines))])  # 写入新文件随机行
oldf.close()
newf.close()
