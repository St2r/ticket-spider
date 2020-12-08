# TicketSpider

一个简单的可以爬取 北京-天津 的高铁票信息的爬虫

## 快速开始

### 配置 Splash 服务端
``` shell
docker run -p 8050:8050 scrapinghub/splash 
```

配置后请在 ```core/settings.py``` 中配置 ```Splash``` 端点

参考 [splash文档](https://splash-cn-doc.readthedocs.io/zh_CN/latest/scrapy-splash-toturial.html)

### 运行爬虫

``` python
python3 main.py
```

结果保存在 ```result.json``` 中

## 实现方案
原方案

通过网络获取 12306 网站网站信息的接口，发现 12306 对接口返回的信息做了加密，解密需要对 JS 进行分析，考虑到复杂度不考虑这个方案。

最终方案

采用 Splash 作为 JavaScript 延时加载的载体，在爬虫中同步等待 12306 网站渲染。渲染结束之后再采用标签解析的方式进行信息提取。



