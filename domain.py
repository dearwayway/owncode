#-*- coding: utf8 -*- 
import os

fp=open("./input.txt",'r+')
fo=file("./output.txt",'w')
for line in fp.readlines():
	#含有com.cn的特殊处理
	dmlist=line.split('.')
	if line.find(".com.cn")==-1:
		domain=dmlist[len(dmlist)-2]+"."+dmlist[len(dmlist)-1]
	else:
		domain=dmlist[len(dmlist)-3]+"."+dmlist[len(dmlist)-2]+"."+dmlist[len(dmlist)-1]
	fo.write(domain)
fo.close()
fp.close()

