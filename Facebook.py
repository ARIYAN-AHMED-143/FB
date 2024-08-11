import requests
import random
import string
import json
import os
from os import system as none
import sys
import hashlib
from faker import Faker
yellow = "\x1b[38;5;208m"
black = "\033[1;30m"
rad = "\033[1;31m"
green = "\033[1;32m"
yelloww = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"
os.system('clear')
none("xdg-open https://t.me/TermuxOpenSource")
print(f"""                              

\x1b[38;5;43md88888b d8888b.         .d8b.   .o88b. 
\x1b[38;5;43m88'     88  `8D        d8' `8b d8P  Y8 
\x1b[38;5;42m88ooo   88oooY'        88ooo88 8P      
\x1b[38;5;41m88~~~   88~~~b. C8888D 88~~~88 8b      
\x1b[38;5;40m88      88   8D        88   88 Y8b  d8 
\x1b[38;5;40mYP      Y8888P'        YP   YP  `Y88P' 
{faltu}{white}UNLIMITED AUTO FACEBOOK ACCOUNT CREATOR{pvt}{green}{rad}
""") 
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
def get_mail_domains():
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print(f'[×] E-mail Error : {response.text}')
            return None
    except Exception as e:
        print(f'[×] Error : {e}')
        return None
def create_mail_tm_account():
    fake = Faker()
    mail_domains = get_mail_domains()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = generate_random_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password":password}       
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(f'')
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'[×] Email Error : {response.text}')
                return None, None, None, None, None
        except Exception as e:
            print(f'[×] Error : {e}')
            return None, None, None, None, None
def register_facebook_account(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {'api_key': api_key,'attempt_login': True,'birthday': birthday.strftime('%Y-%m-%d'),'client_country_code': 'EN','fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod','fb_api_req_friendly_name': 'registerAccount','firstname': first_name,'format': 'json','gender': gender,'lastname': last_name,'email': email,'locale': 'en_US','method': 'user.register','password': password,'reg_instance': generate_random_string(32),'return_multiple_errors': True}
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = _call(api_url, req)
    token=reg['session_info']['access_token']
    
    print(f'''
{faltu}{white}»»Join : @https://t.me/TermuxOpenSource{pvt}{green}{rad}
\033[38;5;220m»»EMAIL : {email}
\033[38;5;221m»»UID : {id}
\033[38;5;222m»»PASSWORD : {password}
\033[38;5;223m»»NAME : {first_name} {last_name}
\033[38;5;224m»»BIRTHDAY : {birthday} 
\033[38;5;225m»»GENDER : {gender}
\033[38;5;225m»»Token : {token}''')
open('fbids.txt','a')
def _call(url, params, post=True):
    headers = {'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'}
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()
for i in range(int(input('[+] How Many Accounts You Want:  '))):
 email, password, first_name, last_name, birthday = create_mail_tm_account()
 if email and password and first_name and last_name and birthday:
  register_facebook_account(email, password, first_name, last_name, birthday)
  