import requests
import json

url_onile = 'https://mova.hexagr.am/property/one?id=d9b98d5c-0929-496e-9db1-b09bae03a3e9'
url ='http://localhost:8080/property/one?id=d9b98d5c-0929-496e-9db1-b09bae03a3e9'
json_file_path = 'file_no_new.json'

# 读取JSON文件
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# for index in range(len(json_data)):
#     # 发送POST请求到本地接口
#     headers = {
#         'Accept': '*/*',
#         'Content-Type': 'application/json'
#     }
#     response = requests.post(url, json=json_data[index], headers=headers)
#     # 检查响应状态码
#     if response.status_code == 204:
#         print('请求成功')
#         # 处理成功响应
#         print(response.json())
#     else:
#         print('请求失败')
#         # 处理失败响应
#         print(response.status_code)
#         print(response.headers)
#         print(response)

for jsonOne in json_data:
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=jsonOne, headers = headers)
    if response.status_code == 204:
        print("请求成功！")
        print(response.status_code)
    else:
        print("请求失败！")
        print(response.status_code)
        print(response.json())

        
        
