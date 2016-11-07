#-*- coding: utf8 -*- 

import os  
from bs4 import BeautifulSoup #引入BeautifulSoup  
  
fp = open("./input.html",'r+')  
soup = BeautifulSoup(fp,"lxml")#根据文件内容新建一个BeautifulSoup对象  

#移除多余代码
soup.find("div",class_="header").extract()
soup.find("script",src="javascript.js").extract()
soup.find("link",href="day-one-html-override.css").extract()
soup.find("div",dir="auto").unwrap()
soup.find("a",class_="do44C0FF").unwrap()

#li节点中加入<p>
for li in soup.find_all('li'):
	newtag=soup.new_tag("p")
	li.string.wrap(newtag)

#副标题样式修改
allh2=soup.find_all('h3')
for h2 in allh2:
	idx=allh2.index(h2)
	titletext='''
<p class="h-n"><em>'''+str(idx+1)+'''</em></p>
<p class="h-l">&nbsp; &nbsp;</p>
'''
	soupnew=BeautifulSoup(titletext,"html.parser")
	h2.insert_before(soupnew)

#增加头部代码
headercode='''
<div class="ww-header">

<div class="left-box">
<div class="left-photo">
</div>
<div class="left-text">产品汪文森特<br/>pm_vincent</div>
</div>


<div class="right-box">
<div class="right-text"><div>读完本文<br/>大约需要</div>
<div class="right-number">6</div>分钟</div>
</div>

</div>

<div style="clear:both;" class="cleardiv"></div>
'''
soupnew=BeautifulSoup(headercode,"html.parser")
soup.find("h1").insert_after(soupnew)


#增加结尾代码
tailcode='''
<p class="we-id"><img alt="" src="http://7xnsj2.com1.z0.glb.clouddn.com/we-id.png"/></p>
'''
soupnew=BeautifulSoup(tailcode,"html.parser")
soup.find("body").append(soupnew)


#增加移动端适配代码
metacode='''
<meta name="viewport" content="width=device-width, initial-scale=1" /> 
'''
soupnew=BeautifulSoup(metacode,"html.parser")
soup.find("link",rel='stylesheet').insert_before(soupnew)

fo=file("temp.html",'wb')
fo.seek(0,os.SEEK_SET)#移动到文件头  
fo.write(str(soup))#重写整个文件  
fo.close()
fp.close()  


#增加intro段落的class，因为beautifulsoup不支持，打开文件直接替换
divpre="""<div class="cleardiv" style="clear:both;"></div>
<div class="intro">
"""
divapp="""</div>
<p class="h-n"><em>1</em></p>
"""
fr=open("./temp.html",'r')
fr2=file("./temp2.html","w")
for line in fr.readlines():
	fr2.write(line.replace('''<div class="cleardiv" style="clear:both;"></div>''', divpre))
fr2.close()
fr.close()

fr=open("./temp2.html",'r')
fr2=file("./output.html","w")
for line in fr.readlines():
	fr2.write(line.replace('''<p class="h-n"><em>1</em></p>''', divapp))
fr2.close()
fr.close()
os.remove("./temp.html")
os.remove("./temp2.html")



