# coding=utf-8
import requests

proxies = {"http":"http://163.177.151.23:80"}
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

response=requests.get("http://www.baidu.com",proxies=proxies)
print(response.status_code)

