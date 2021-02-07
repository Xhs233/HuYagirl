import requests#导入请求库
import re#导入正则表达式


url = 'http://www.weixinbqb.com/plus/list.php?tid=8&TotalResult=3203&PageNo=4'#嵌入要爬取的网址

res = requests.get(url)#创建res函数，请求得到表情包官网的链接

reg = '<img src="(.*?)" alt=".*?">'#创建正则表达式（也就是要请求的表情包的格式）这里的“<img scr="因为不知道表请包链接所以用”.*?"来代替，同理alt="这里也不知道图片编号所以用“.*?”来代替
urls = re.findall(reg,res.text)#创建urls函数
reg = '<img src=".*?" alt="(.*?)">'#创建正则表达式（也就是要请求的表情包的格式）这里的“<img scr="因为不知道表请包链接所以用”.*?"来代替，同理alt="这里也不知道图片编号所以用“.*?”来代替
names = re.findall(reg,res.text)#创建names函数

for url,name in zip(urls,names):
    print('http://www.weixinbqb.com'+url)#注意缩进！！！！！！！！
    #这里的url是将所抓取的表情包的链接变城可以点开的链接

    #下面是把所请求到数据的名字中间的<b>和</b>去掉
    name = name.replace('<b>','')
    name = name.replace('</b>','')
#把数据保存本地
    image = requests.get('http://www.weixinbqb.com'+url)
    with open("./表情包"+name+".gif",'wb')as f:
        f.write(image.content)
        print('<%s>下载成功'% name)

