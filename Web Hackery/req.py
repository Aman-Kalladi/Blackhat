import urllib.parse
import urllib.request
import requests

url = 'http://boodelyboo.com'
with urllib.request.urlopen(url) as response:  # GET
    content = response.read()
    
print(content)

info = {'user': 'tim', 'passwd': '31337'}
data = urllib.parse.urlencode(info).encode()  # data is now of type bytes
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:  # POST
    content = response.read()

print(content)

response = requests.get(url)  # GET
data = {'user': 'tim', 'passwd': '31337'}
response = requests.post(url, data=data)  # POST
print(response.text)  # response.text = string
response.content  # = bytestring

