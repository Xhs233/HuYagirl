#获取虎牙主播封面功能
from random import choice#从choice库中导出random程序
from os import makedirs#从makedirs库中导出os程序
import requests#导入请求库
import re#导入re库


'''''
创建爬虫返回照片的文件夹
'''''
try:
    makedirs("虎牙图片") #尝试在当前路径创建文件夹用于存放图片
except:
    pass


#创建请求模块可以使用def函数
def mnn():
    url = "https://huya.com/g/" + choice(["2168","2633","4079"]) #随机爬取颜值、二次元、交友区
    html = requests.get(url).text  #经测试无需伪装协议头
    reg = '<img class="pic" data-original="(.*?)?imageview/4/0/w/338/h/190/blur/1'  #创建正则表达式
                                 #这里的original是原版的意思#这里的imageview是图片浏览的意思w是照片的宽h是照片的高bliur是模糊的意思
    data = re.findall(re.compile(reg),html)  #正则匹配上方的正则表达式里规定的规则的图片
    return data#返回数据
    
data = mnn()  #调用函数获取返回数组
for i in range(len(data)):  
    img = requests.get(data[i]).content
    i += 1  #这里是为了方便计数
    open("虎牙图片/%d.jpg"%(i),"wb").write(img)
    print("已下载%d/%d张"%(i,len(data)))
input("按任意键退出\n")
    



    #注：def函数的使用危：def________这里可以自定义一个函数名________()def函数名后面的括号内可以存储所要运行的程序方便
#到时候用到的时候提取
