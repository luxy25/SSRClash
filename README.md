# 脚本功能

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)



  - 本地生成CLash配置文件
  - Clash API
  - Quantumult X API 实验阶段
 

# 功能介绍

  - 初级：建议使用SSR_CLash_NoGroup.py <br/>
    没有节点分组，默认不配置DNS。不再更新
  - 高级：建议使用SSR_Clash_HttpServer.py  <br/>
    此版解码方法优化，支持大多数机场。 <br/>
    运行后托管地址输入http://127.0.0.1:8964/?+订阅地址
  - CLashAPI：建议使用SSR_Clash_API.py。 <br/>
   部署在VPS上，需要python3环境。同目录下放置general.yml 和lrules.yml 
  - QuantumultAPI：建议使用qx.py。 <br/>
   部署在VPS上，需要python3环境。

   CLashAPI调用方式:
  - SSR订阅到Clash <br/>
   调用地址为：http://ip:10086/订阅地址  <br/>
   其中订阅地址中的/替换为！ <br/>
   默认故障切换在前，如果你想让手动切换在前在最后加上@@yes
  - SSR订阅筛选
   http://ip:10086/ssr/订阅地址   <br/>
   其中订阅地址中的/替换为！ <br/>
   假设只想要香港和杭港节点，加上@香港@美国 <br/>
   假设你只想要香港1倍节点和杭港5倍节点，加上@香港&1倍@杭港&5倍 <br/>
   说明：如果报错，说明你的客户端不支持中文URL，先URL_Encode一下（Google） 
  - 客制化SSR_Clash订阅
   调用地址为地址为http://ip:10086/订阅地址 <br/>
   其中订阅地址中的/替换为！  <br/>
   假设只想要香港和杭港节点，加上@香港@美国 <br/>
   假设只想要香港1倍节点和杭港5倍节点，为@香港&1倍@杭港&5倍 默认故障切换在前，如果你想让手动切换在前在最后加上@@yes <br/>
   说明：如果报错，说明你的客户端不支持中文URL，先URL_Encode一下（Google）<br/>
   QuantumultAPI调用方式:
   - http://ip:2333/订阅地址1@标签1@@订阅地址2@标签2 <br/>
    其中订阅地址中的/替换为！ <br/>
    标签可不填写，默认标签为傻吊家的节点

# 联系我
   - https://t.me/NicoNewBeee


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
