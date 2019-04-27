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
##### 创建profile记录  
调用接口：http://127.0.0.1/api/v1/profiles  
调用方法：POST  
参数格式：JSON  
输入参数：[nickname, signature]  
调用示例：
```bash
curl -H "Content-type: application/json" -d '{"nickname":"lalala223","signature":"积硅步，至千里"}' -X POST http://127.0.0.1:5000/api/v1/profiles
```
返回示例：
```json
{
    "code": 0,
    "msg": "添加数据成功～",
    "data": null
}
```

##### 获取profile记录  
调用接口：http://127.0.0.1/api/v1/profiles  
调用方法：GET  
参数格式：Query String  
输入参数：[page_num, page_size]  
调用示例：
```bash
curl http://127.0.0.1:5000/api/v1/profiles?page_num=1&page_size=10
```
返回示例：
```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "page_num": 1,
        "page_size": 10,
        "total": 1,
        "items": [
            {
                "id": 1,
                "nickname": "lalala223",
                "signature": "积硅步，至千里"
            }
        ]
    }
}
```