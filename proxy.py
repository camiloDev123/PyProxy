import requests # this proxy manager is for requests module!
import time
import os
import sys

# session = requests.Session()

def format_proxy(proxy):
    splittedStr = proxy.split(":")

    if len(splittedStr)==2:
        ip_port = True
    
    else:
        ip_port = False
    
    if ip_port==True:
        ip = splittedStr[0]
        port = splittedStr[1]

        return {
            "https": f"https://{ip}:{port}",
            "http": f"http://{ip}:{port}"
        }

    elif ip_port==False:
        ip = splittedStr[0]
        port = splittedStr[1]
        user = splittedStr[2]
        pw = splittedStr[3]

        return {
            "https": f"http://{user}:{pw}@{ip}:{port}",
            "http": f"http://{user}:{pw}@{ip}:{port}"
        }
    
# proxy = format_proxy("sdfsdfsdf:gdfgdfgdf:kjuoiuoi:uewrrwer")
# session.proxies = proxy
# url = "https://api.myip.com"
# resp = session.get(url)
# print(resp.text)