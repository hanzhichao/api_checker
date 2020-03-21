# Api Checker
米兔-修正版 根据教程https://my.oschina.net/u/3041656/blog/820023编写

* 教程中 Log.py class Log中少写了get_result_path和get_logger两个方法,已补全
* 教程中 runAll.py中少了class名，init方法及run中的resultPath,on_off,已补全
* 修正导包问题
* 由于原生HTMLTestRunner.py不支持python3, 使用GitHub上某个人的美化修改版本：HTMLTestRunnerCN.py

## 特性
- 配置文件使用config
- 数据文件使用excel
- 运行用例通过caseList.txt指定
- 支持baseurl

## 优点
- 通过caselist.txt控制执行的用例
- 使用excel管理api和data
- 配置中有是否发送邮件开关

## 缺点

- 不支持session和cookies
- 不支持Auth和签名
- 不支持并发
- 不支持场景和压测
- 可以使用nose/pytest代替unittest
- Log只支持写入文件的log不支持运行时的终端显示log
