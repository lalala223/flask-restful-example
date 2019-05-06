# Flask-Restful 项目结构示例
#### 安装依赖包
```
python install -r requirements.txt
```

#### 创建数据表
```
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```

#### debug模式启动
```
python manager.py debug
```

#### 生产模式启动
```
python manager.py run
```

#### 示例APIs
##### 创建一条profile数据  
调用接口：http://127.0.0.1/api/v1/profiles  
调用方法：POST  
参数格式：JSON  
输入参数：[nickname, signature]  
调用示例：
```bash
curl -H 'Content-type: application/json' -d '{"nickname":"lalala223","signature":"积硅步，至千里!"}' -X POST 'http://127.0.0.1:5000/api/v1/profiles'
```
返回示例：
```json
{
    "code": 0,
    "msg": "添加数据成功～",
    "data": null
}
```

##### 获取分页profile数据  
调用接口：http://127.0.0.1/api/v1/profiles  
调用方法：GET  
参数格式：Query String  
输入参数：[page_num, page_size]  
调用示例：
```bash
curl 'http://127.0.0.1:5000/api/v1/profiles?page_num=1&page_size=10'
```
返回示例：
```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "page_num": 1,
        "page_size": 10,
        "total": 3,
        "items": [
            {
                "id": "2v5y45gr",
                "nickname": "test1",
                "signature": "积硅步，至千里!"
            },
            {
                "id": "m6k1zl84",
                "nickname": "test2",
                "signature": "你喜欢青草还是羽毛。"
            },
            {
                "id": "jqlpw5v6",
                "nickname": "test3",
                "signature": "吃个苹果吧~"
            }
        ]
    }
}
```

##### 获取一条profile数据  
调用接口：http://127.0.0.1/api/v1/profiles/[id]  
调用方法：GET  
参数格式：URL PARAM  
输入参数：[id]  
调用示例：
```bash
curl 'http://127.0.0.1:5000/api/v1/profiles/2v5y45gr'
```
返回示例：
```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "id": "2v5y45gr",
        "nickname": "test1",
        "signature": "积硅步，至千里!"
    }
}
```

##### 修改一条profile数据  
调用接口：http://127.0.0.1/api/v1/profiles/[id]  
调用方法：PUT  
参数格式：URL PARAM + JSON  
输入参数：[id, nickname, signature]   
调用示例：
```bash
curl -H 'Content-type: application/json' -d '{"nickname":"test1","signature":"喜欢独处，热爱自由!"}' -X PUT 'http://127.0.0.1:5000/api/v1/profiles/2v5y45gr'
```
返回示例：
```json
{
    "code": 0,
    "msg": "修改数据成功～",
    "data": null
}
```

##### 删除一条profile数据   
调用接口：http://127.0.0.1/api/v1/profiles/[id]  
调用方法：DELETE  
参数格式：URL PARAM  
输入参数：[id]   
调用示例：
```bash
curl -X DELETE 'http://127.0.0.1:5000/api/v1/profiles/2v5y45gr'
```
返回示例：
```json
{
    "code": 0,
    "msg": "删除数据成功～",
    "data": null
}
```
