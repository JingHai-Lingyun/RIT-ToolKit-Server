# 接口文档

### 接口路径

- `/waypoint/getAllWaypoint`

### 接口描述

- 获取所有路径点

### 接口访问类型

- GET

### 接口参数
| 参数名 | 参数类型 | 是否必填 | 参数描述 |
| ------ | -------- | --------- | ----------- |
| updateUserID | string | 是 | 请求的用户名称 |

### 请求示例

```http
GET /waypoint/getAllWaypoint?&updateUserID=test HTTP/1.1
Host: http://154.7.177.68
```

### 响应示例
###### 常规情况
```http
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "name": "\u57fa\u5730 x \u4e3b\u4e16\u754c\u4ea4\u6613\u6240", 
        "x": "-172", 
        "y": "102", 
        "z": "321", 
        "dim": "Overworld", 
        "ID": "LingyunAwA"
    }, 
    {
        "name": "\u5c0f\u94b1\u94b1\u751f\u4ea7\u673a\uff08\u88ad\u51fb\u5854\uff09", 
        "x": "70", 
        "y": "128", 
        "z": "7", 
        "dim": "Nether", 
        "ID": "ToastBreadMc"
    }
]
```

###### 路径点列表为空时返回
```http
HTTP/1.1 200 OK
Content-Type: application/json

[]
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