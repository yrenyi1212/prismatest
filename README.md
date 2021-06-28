# prismatest  
### pytest+allure test for prisma   
___
``亲爱的同事，当你读到这份代码时...(*^_^*)``
___
**介绍**  

Prisma项目接口测试，此代码框架可以适用我们内部大部分接口测试任务，仅需稍加调整即可，比如请求头、请求参数的预处理，只需要调整对应的fixture  
- 分支master，使用json进行参数化处理，代码自动发现、自动注册测试接口参数化配置，请求头及请求参数使用fixture自动处理，自动对响应结果进行标记检查，过程无需干预，代码更简单、更智能,推荐使用
- 分支test，使用list进行参数化处理，参数配置需要手动写入各个test方法，请求头及请求参数使用装饰器处理，不再维护；    

**数据格式说明**  
data目录json文件为测试数据  
title，payload，expect必须定义，header、mark为可选字段
```json
{
      "title": "定义用例标题", 
      "header": {
        "HTTP_X_FORWARDED_FOR": "定义请求头，可以定义多个"
      },
      "payload": {
        "key": "定义POST请求的JSON数据"
      },
      "expect": {
        "key1": "定义预期响应内容，允许嵌套，代码自动检查每个字段预期与响应是否一致",
        "key2": {
          "key3": "嵌套响应字段检查"
      },
      "mark": {
        "value": "标记测试结果,当前只允许标记xfail",
        "message": "标记为xfail的原因"
      }
    }
}
```