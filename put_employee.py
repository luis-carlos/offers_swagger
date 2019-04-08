import requests
import json

def update_employee():
    apex_api_url = 'https://apex.oraclecorp.com/pls/apex/lcg-demo/hr/employees/7839'
    payload = {'ename':'REY', 'job':'DIRECTOR', 'mgr':'7838', 'hiredate':'05/01/1981', 'sal':'3500', 'deptno':'1'}
    r = requests.put(apex_api_url,data=json.dumps(payload))
    print(r.status_code)
    print(r.content)

update_employee()
    
    
