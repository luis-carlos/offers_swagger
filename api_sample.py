import requests

def get_data():
    apex_api_url = 'https://apex.oraclecorp.com/pls/apex/lcg-demo/hr/employees/7839'
    request_data = requests.get(apex_api_url)
    return request_data.json()

print(get_data())
    
