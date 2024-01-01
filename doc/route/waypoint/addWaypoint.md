# 接口文档

### 接口路径

- `/waypoint/addWaypoint`

### 接口描述

- 添加路径点

### 接口访问类型

- POST

### 接口参数

| 参数名          | 参数类型   | 是否必填 | 参数描述     |
| ------------ | ------ | ---- | -------- |
| waypointName | string | 是    | 路径点名称    |
| X            | int    | 是    | 路径点 X 坐标 |
| Y            | int    | 是    | 路径点 Y 坐标 |
| Z            | int    | 是    | 路径点 Z 坐标 |
| Dim          | string | 是    | 路径点维度    |
| updateUserID | string | 是    | 请求的用户名称  |

注：Dim 为 Overworld | Nether | The End 三项中的一项

### 请求示例

```http
POST /waypoint/addWaypoint HTTP/1.1
Host: http://154.7.177.68
Content-Type: application/x-www-form-urlencoded

waypointName=test&X=10&Y=10&Z=10&Dim=Overworld&updateUserID=test
```

### 响应示例

###### 常规情况

```http
HTTP/1.1 200 OK
```

###### 未给参数 `waypointName` 或 `X` 或 `Y` 或 `Z` 或 `Dim` 时

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "status": "FAIL",
    "code": 400,
    "message": "缺少参数 waypointName"
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
