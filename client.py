import requests, json

#resp = requests.get("http://127.0.0.1:5000/hello/Nikola")

poster = requests.post(
    url="http://127.0.0.1:5000/poster/",
    params={'my-param-name': 'param-value'},
    headers={'my-header-name': 'header-value'},
    json=json.dumps({'some': 'value'})
)

print(poster.status_code)
print(poster.text)
print(poster.reason)
print(poster.links)
print("Headers: ", poster.headers)
print("json: ", poster.json)