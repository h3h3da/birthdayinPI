# birthdayinPI
Get birthday position after dot in Pi.

## 简介

birthdayinPI是一个查询八位生日数字（格式如20210314）在π中首次出现位置的工具。
`query_server`文件夹下包含一个result.txt文件其中包含了使用`inti_pos_lib`下的程序初始化生成的位置数据。
可以直接运行来查询结果。

目前较小的数据集支持从1910-01-01——2021-12-31这一个时间段的查询，后续会更新数据集支持更大时间范围内的查询。

## 运行方法

直接运行 `python3 getpos.py` 即可。

## 接入微信公众号
我们可以把服务接入微信公众号，这样就可以直接通过公众号来查询位置啦~ 
【菜鸟安全笔记】大家快来关注一波呀~
![image](https://user-images.githubusercontent.com/20582659/111067411-1643c880-84ff-11eb-91e7-6b8d5f3b3fa5.png)
### 接入步骤
首先要有一个公众号，这里注册公众号的步骤就不详细说了。登录微信公众平台管理端，在最下面找到开发-基本配置项：
![image](https://user-images.githubusercontent.com/20582659/111067387-fb715400-84fe-11eb-8cf2-31e016471e4a.png)
按照要求配置好服务器：
![image](https://user-images.githubusercontent.com/20582659/111067485-70dd2480-84ff-11eb-8e71-b658ee54468f.png)
在`query_server/app.py` 中已经实现了服务器认证和查询恢复的功能，其中`query_server/config.py`中的`Token`为服务器配置过程中你自定义的Token，修改为自己的`Token`后直接运行在配置好的服务器的80端口即可。
可以执行`nohup ./start.sh  > /dev/null 2>&1 &` 直接放后台执行。
## 欢迎大家关注我的公众号
各种干货文章以及好玩的功能都在等着你哦！
![image](https://user-images.githubusercontent.com/20582659/111067711-68d1b480-8500-11eb-8526-acdddb014433.png)


