#encoding=utf8
import urllib
import urllib2
import os

picurl="http://gqzzwr.duapp.com/img.php?name=dycj201542&page="
picNum=
save_path="/Users/Weiwei/Desktop"
imgData = urllib2.urlopen(picurl).read()
# 给定图片存放名称
fileName = save_path + "/001.jpg"
# 文件名是否存在
#if os.path.exists(fileName):
output = open(fileName,'wb+')
output.write(imgData)
output.close()
print "Finished download \n"
print "运行完成"
