# Flask-RESTful Example 
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

#### Tests
```
python -m tests.testapp
```