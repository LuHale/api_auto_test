import requests
import json

class api_request:

    def __init__(self,base_url):
        self.base_url = base_url
        self.result = None
    def request_get(self,api_name,data):
        self.result = requests.get(self.base_url + api_name,data=data)

    def request_post(self,api_name,data):
        self.result = requests.post(self.base_url + api_name,data=data)



if __name__ == '__main__':
    base_url = "http://api.kepuchina.com.cn/"
    api_name = "account/login?no_check=1"
    data = {
        "mobile":18665708701,
        "password":111111,
        "source":2,
        "country_code":86,
        "unique_identifier":"5EF0218223004869",
        "from":"android",
        "v":"2.0.0",
        "app_version":"2.0.1"
    }
    result = api_request(base_url)
    result.request_post(api_name,data)
    print(result.result.status_code)
    print(result.result.url)
    print(result.result.json())