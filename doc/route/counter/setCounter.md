# 接口文档

### 接口路径

- `/counter/setCounter`

### 接口描述

- 删除指定计数器

### 接口访问类型

- PATCH

### 接口参数

| 参数名          | 参数类型   | 是否必填 | 参数描述    |
| ------------ | ------ | ---- | ------- |
| counterName  | string | 是    | 计数器名称   |
| counterValue | string | 是    | 要设置的值   |
| updateUserID | string | 是    | 请求的用户名称 |

### 请求示例

```http
PATCH /counter/setCounter HTTP/1.1
Host: http://154.7.177.68
Content-Type: application/x-www-form-urlencoded

counterName=test&counterValue=12&updateUserID=test
```

### 响应示例

###### 常规情况

```http
HTTP/1.1 200 OK
```

###### 未给参数 `counterName` 或 `counterValue` 时

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "status": "FAIL",
    "code": 400,
    "message": "缺少参数 counterName 或 counterValue"
}
```

###### 未给参数 `updateUserID` 时

```http
HTTP/1.1 403 Forbidden
Content-Type: application/json

{
    "status": "FAIL",
    "code": 403,
    "message": "缺少参数 updateUserID"
}
```

###### 服务器发生处理异常时

```http
HTTP/1.1 500 Internal Server Error
Content-Type: application/json

{
    "status": "FAIL",
    "code": 500,
}
```
