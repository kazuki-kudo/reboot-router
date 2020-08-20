#! /usr/bin/env python3

# This python script reboots the BUFFALO Internet Router.
# Target model : WHR-1166DHP
#
# Set environment variables when calling the script
# * RT_HOST : router hostname or ip address.
# * RT_ADMIN_USER : router admin user. default 'admin'
# + RT_ADMIN_PASS : router admin password.  default 'password'

import os,requests,sys,bs4
import time

import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('start')


# environment variables read
rt_host = os.getenv('RT_HOST')
if rt_host == None:
    logging.error('ENVVAR RT_HOST is none')
    sys.exit(1)

rt_admin_user = os.getenv('RT_ADMIN_USER')
if rt_admin_user == None:
    rt_admin_user = 'admin'

rt_admin_pass = os.getenv('RT_ADMIN_PASS')
if rt_admin_user == None:
    logging.error('ENVVAR RT_ADMIN_PASS is none')
    sys.exit(1)

HOST_URL = 'http://' + rt_host + '/init.html'
BASIC_AUTH = (rt_admin_user,rt_admin_pass)

try:
    # screen 0
    # dummy request. possible 401 auth error.
    res0 = requests.get(HOST_URL,auth=BASIC_AUTH)
    time.sleep(2)

    # screen 1
    res1 = requests.get(HOST_URL,auth=BASIC_AUTH)
    res1.raise_for_status()
    
    html1 = bs4.BeautifulSoup(res1.text,'html.parser')
    ele = html1.select('input[name="nosave_session_num"]')[0]
    time.sleep(2)

    # screen 2
    nosave_session_num = ele.get('value')
    
    payload = {'nosave_reboot': '1', 'nosave_session_num': nosave_session_num}
    res2 = requests.post(HOST_URL + '?screen2',data=payload,auth=BASIC_AUTH)
    res2.raise_for_status()

    logging.info('complete')

except Exception as exc:
    logging.error('error:{}'.format(exc))
    sys.exit(1)




