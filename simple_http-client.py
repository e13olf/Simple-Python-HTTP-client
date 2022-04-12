#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'https://account.shodan.io/login',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
}
# Request Body Parameters from Request Body/ page source
login_data = {
             'username' : 'username',
             'password' : 'pass',
             'grant_type' : 'password',
             'continue' : 'https://account.shodan.io/'
  }

with requests.Session() as s:
    url = 'https://account.shodan.io/login'
    r = s.get(url,headers=headers)
    #print(r.content) # to find name of csrf_token and form_build_id
    soup = BeautifulSoup(r.text, 'lxml')
    csrf_token = soup.find('input',attrs = {'name':'csrf_token'})['value']
    login_data['csrf_token'] = csrf_token
   
    r = s.post(url,data=login_data, headers = headers, allow_redirects=True)

    if 'login' in r.text:
        print ('Failed!')
        print('Script Exiting ...')
    elif 'logout' in r.text:
        print('Logged in')
        print('Script Exiting ...')
