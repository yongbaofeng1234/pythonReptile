# coding:utf-8
from bs4 import BeautifulSoup
"""
  1. 常见的网页解析器：正则表达式模块  import re，模糊匹配
  2. Python自带解析器html.parser；
  3. 第三方解析器BeautifulSoup，比较强大；
  4. requests；
  5. lxml解析html或者xml网页；
  
  1 ==> 主要是牧户匹配
  2,3,4,5 ==> 主要是结构化解析
  
"""
# 详细说明
from urllib import urlopen
"""
   HTML网页  ==> 创建一个BeautifulSoup对象  ==> 搜索节点
   find_all和find的区别很容易
   ==>  访问接待你名称+属性+文字
   
   eg1:
   <a href="123.html" class="atricle_link"> Python </a>
   soup=BeautifulSoup(
       html_doc,
       'html.parser',
       from_encoding='utf-8'
   )
   
   find_all(name.attr,string)
   
   eg2:
   node=aoup.find_all('div',href=re.compile(r'/view/\d+\.htm'),string='Python')
   node.name;
   node['href']
   node.get_text()
"""
url="http://www.yangxianpku.com"
response=urlopen(url).read()
# print response
soup=BeautifulSoup(response,'html.parser',from_encoding='utf-8')
links=soup.find_all('a')
linkss=soup.find_all('a',class_='www')
for link in links:
    print link.name,link['href'],link.get_text()
    






