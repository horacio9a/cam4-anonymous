# Cam4 Remote Anonymous STREAMLINK Recorder v.1.1.1 by horacio9a for Python 3.9.1
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, command
urllib3.disable_warnings()
from urllib3 import PoolManager
from urllib.parse import quote
from urllib.parse import unquote
from colorama import init, Fore, Back, Style
from termcolor import colored
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

init()
print()
print(colored(' => START <=', 'white', 'on_blue'))

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://www.cam4.com/{}'.format(model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = quote(r.data)
dec= unquote(enc)

if 'showState' in dec:
  status0 = dec.split("showState: '")[1]
  status = status0.split("'")[0]
  if len(status) > 0:
    try:
      gender0 = dec.split(' gender-')[1]
      gender1 = gender0.split('" t')[0]
      gender = gender1.split('="')[1]
    except:
      gender = '-'

    try:
      orientation0 = dec.split('orientation ')[1]
      orientation1 = orientation0.split('</')[0]
      orientation = orientation1.split('>')[1]
    except:
      orientation = '-'

    try:
      country0 = dec.split('"country"')[1]
      country1 = country0.split('" t')[0]
      country = country1.split('t="')[1]
    except:
      country = '-'

    try:
      age0 = dec.split('Age:</')[1]
      age1 = age0.split('</')[0]
      age = age1.split('">')[1]
    except:
      age = '-'

    try:
      loc0 = dec.split('Location:</')[1]
      loc1 = loc0.split('</')[0]
      loc2 = loc1.split('">')[1]
      loc3 = re.sub(',', '', loc2)
      loc = re.sub(' ', '', loc3)
    except:
      loc = '-'

    try:
      sta0 = dec.split('Status:</')[1]
      sta1 = sta0.split('</')[0]
      sta = sta1.split('">')[1]
    except:
      sta = '-'

    try:
      room0 = dec.split('room":"')[1]
      room = room0.split('"')[0]
    except:
      room = '-'

    try:
      ms0 = dec.split('Member since:</')[1]
      ms1 = ms0.split('</')[0]
      ms2 = ms1.split('">')[1]
      ms3 = re.sub(' ', '-', ms2)
      ms = re.sub(',', '', ms3)
    except:
      ms = '-'

    try:
      eth0 = dec.split('Ethnicity:</')[1]
      eth1 = eth0.split('</')[0]
      eth2 = eth1.split('">')[1]
      eth = re.sub(' ', '', eth2)
    except:
      eth = '-'

    vpu0 = dec.split('videoPlayUrl":"')[1]
    vpu = vpu0.split('"')[0]

    wcdn = vpu.split('-')[1]

    hlsurl = 'https://cam4-hls.xcdnpro.com/{}/cam4-origin-live/{}_aac/playlist.m3u8'.format(wcdn,vpu)
 
    print ((colored('\n => Room: ({}) * Member since: ({}) * Room status: ({}) <=', 'white', 'on_blue')).format(room,ms,status))
    print ((colored('\n => Age: ({}) * Gender: ({}) * Orientation: ({}) * Status: ({}) <=', 'white', 'on_blue')).format(age,gender,orientation,sta))
    print ((colored('\n => Country: ({}) * Location: ({}) * Ethnic: ({}) <=', 'white', 'on_blue')).format(country,loc,eth))
 
    timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
    path = config.get('folders', 'output_folder')
    streamlink = config.get('files', 'streamlink')
    filename = room + '_C4_' + timestamp + '.mp4'
    pf = path + filename
    print ((colored('\n => SL-REC >>> {} <<<', 'white', 'on_red')).format(filename))
    print()
    command = ('{} hls://{} best -Q --hls-live-edge 1 --hls-playlist-reload-attempts 9 --hls-segment-threads 3 --hls-segment-timeout 5.0 --hls-timeout 20.0 -o {}'.format(streamlink,hlsurl,pf))
    os.system(command)
    sys.exit()

  else:
    print(colored('\n => Model is offline <=', 'white','on_red'))
    print()
    print(colored(' => END <=', 'white','on_blue'))
    sys.exit()

else:
   print(colored('\n => Page Not Found <=', 'white','on_red'))
   print()
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()