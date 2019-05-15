#!/usr/bin/env python
 
import sys
import requests
from bs4 import BeautifulSoup
 
try:
    r = requests.get('https://download.microsoft.com/download/0/1/8/018E208D-54F8-44CD-AA26-CD7BC9524A8C/PublicIPs_20170515.xml')
except Exception as e:
    print('Error making https request : {}'.format(e))
    sys.exit(1)
 
if r.status_code == 200:
    xml_data = BeautifulSoup(r.text, "lxml")
    ip_range = xml_data.find_all('iprange')
    for ip in ip_range:
        print(ip.get('subnet'))
