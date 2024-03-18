# Cam4 Remote Anonymous STREAMLINK Recorder v.2.1.0 by horacio9a for Python 2.7.18
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, requests, random, command
urllib3.disable_warnings()
from urllib3 import PoolManager
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import configparser
Config = configparser.ConfigParser()
Config.read('config.ini')
country_domain = Config.get('settings', 'country_domain')

init()
print
print(colored(' => START <=', 'white', 'on_blue'))
print

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://{}.cam4.com/rest/v1.0/profile/{}/streamInfo'.format(country_domain, model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = (r.data)
dec=urllib.unquote(enc)

if len(dec) > 0:
    hlsur2 = dec.split('cdnURL":"')[1]
    hlsurl = hlsur2.split('"')[0]

    timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
    stime = str(time.strftime('%H:%M:%S'))
    path = Config.get('folders', 'output_folder')
    streamlink = Config.get('files', 'streamlink')
    filename = model + '_C4_' + timestamp + '.mp4'
    pf = path + filename
    print (colored(' => SL-REC => {}  (  Size  @   Speed   )', 'white', 'on_red')).format(filename)
    print
    command = ('{} hls://{} best -Q --hls-live-edge 1 --hls-playlist-reload-attempts 9 --hls-segment-threads 3 --hls-segment-timeout 5.0 --hls-timeout 20.0 -o {}'.format(streamlink,hlsurl,pf))
    os.system(command)
    sys.exit()

else:
   print(colored(' => Model is offline or wrong name <=', 'white','on_red'))
   print
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()
