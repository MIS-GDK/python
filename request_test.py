import requests

url = "https://www.baidu.com/s"
kv = {"key1": "nihao"}
r = requests.request("GET", url, params=kv)
print(r.url.query_string)

