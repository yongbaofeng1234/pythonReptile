#! -*-coding:utf-8 -*-
import urllib2
import cookielib

url1="http://www.baidu.com"
url2="http://www.yangxianpku.com"
url3="http://www.liangweizhi.com"

# Method-1
#respose=urllib2.urlopen(url, data, timeout, cafile, capath, cadefault, context)
respose1=urllib2.urlopen(url1)    #  直接请求
print respose1.getcode()          #  读取请求返回状态马，200则表示请求返回成功；
content=respose1.read()           #  读取内容
print len(content)


# Method-2  添加：data+ http header头信息  ()==>urllib2.Request对象==>urlopen方法
request=urllib2.Request(url2)                           #  创建请求对象
#request.add_data('a','1')                              #  网对象里添加数据
request.add_header('User-Agent', 'Mozilla/5.0')         #  添加请求头信息，伪装成特定的浏览器
respose2=urllib2.urlopen(request)                       #  访问获取结果

# Method-3  添加特殊情景处理器：
"""
  1.  HTTPCookieProcessor   需要登录才能访问，需要添加cookie的处理；
  2.  ProxyHandler          需要使用代理才能访问
  3.  HTTPSHandler          https加密方式访问；
  4.  HTTPRedirectHandler   网页相互自动跳转关系
  
  1+2+3+4 ==> opener=urllib2.build_opener(handler) ==> urllib2.install_opener(opener) ==>  urllib2.urlopen
"""
cj=cookielib.CookieJar()                                   # 创建cookie容器，即cookie的handler
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor)   # 创建opener
urllib2.install_opener(opener)                             # 安装opener
respose3=urllib2.urlopen(url3)