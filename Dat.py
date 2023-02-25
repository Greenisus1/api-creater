Name = input(‘enter your name’)
If name = ‘Liam’:
Print( ‘hello Sarah! ‘)
Else: print(‘your not Liam’)

import requests

r = requests.post('https://<subdomain>.onelogin.com/auth/oauth2/v2/token',
  auth=('ONELOGIN CLIENT ID','ONELOGIN CLIENT SECRET'),
  json={
    "grant_type": "client_credentials"
  }
)
response = r.json()

print(response['access_token'])
      import requests

r = requests.post('https://<subdomain>.onelogin.com/auth/oauth2/v2/token',
  auth=('ONELOGIN CLIENT ID','ONELOGIN CLIENT SECRET'),
  json={
    "grant_type": "client_credentials"
  }
)
response = r.json()

print(response['access_token'])
      
