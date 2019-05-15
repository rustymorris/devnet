#!/usr/bin/env python

import sys
import requests

try:
    r = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
except Exception as e:
    print('Error making https request : {}'.format(e))
    sys.exit(1)


if r.status_code == 200:
    for item in r.json().get('prefixes'):
        print(item.get('ip_prefix'))


for num in [1, 2, 3, 4]:
    print(num)
