import requests

x=requests.get('https://api.exchangeratesapi.io/latest')
print(x.text)
print(x.status_code)
print(x.json())

import json

result_dict=json.loads(x.text)
print(result_dict)
print(result_dict['rates']['CAD'])

#try...except/catch
import requests
from requests.exceptions import HTTPError

url='https://api.github.com'

try:
    response=requests.get(url)
    response.raise_for_status() #yeu cau request throw error
except HTTPError as http_err:
    print('Http error: {}'.format(http_err))
except Exception as err:
    print('Error: {}'.format(err))
else:
    print('success')

#reuest with parameter
response=requests.get('https://api.github.com/search/repositories',params={'q':'requests+languages:python'})
print(response.json())    
    
    

    
    
