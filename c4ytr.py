# Cam4 Remote Anonymous YTDL Recorder v.1.0.8 by horacio9a for Python 2.7.14

import sys, os, urllib, urllib3, ssl, re, time, datetime, command
urllib3.disable_warnings()
from urllib3 import PoolManager
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.cfg')

init()
print(colored('\n => START <=', 'yellow', 'on_blue'))

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://www.cam4.com/{}'.format(model)
user_agent = {'user-agent': 'Mozilla/5.0 (Android; Mobile; rv:14.0) ..'}
http = urllib3.PoolManager(10, headers=user_agent)
r = http.urlopen('GET',url)
enc = (r.data)
dec=urllib.unquote(enc).decode()

state0 = dec.split("showState: '")[1]
state = state0.split("'")[0]

if len(state) > 0:
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

 if len(vpu) > 80:
    print(colored('\n => TRY AGAIN <=', 'yellow','on_blue'))
    time.sleep(3)
    print(colored('\n => END <=', 'yellow','on_blue'))
    time.sleep(1)
    sys.exit()
 else:
    pass

 wcdn = vpu.split('-')[1]

 print (colored('\n => Room: ({}) * State: ({}) * Member since: ({}) <=', 'white', 'on_blue')).format(room,state,ms)
 print (colored('\n => Age: ({}) * Location: ({}) * Status: ({}) * Ethnic: ({}) <=', 'yellow', 'on_blue')).format(age,loc,sta,eth)

 hlsurl1 = 'https://lwcdn-{}.cam4.com/cam4-origin-live/ngrp:{}_all/playlist.m3u8'.format(wcdn,vpu)
 hlsurl2 = 'https://lwcdn-{}.cam4.com/cam4-origin-live/amlst:{}_aac/playlist.m3u8'.format(wcdn,vpu)
 hlsurl = 'https://lwcdn-{}.cam4.com/cam4-origin-live/{}_aac/playlist.m3u8'.format(wcdn,vpu)
 hls_url0 = dec.split("hlsUrl: '")[1]
 hls_url1 = hls_url0.split("'")[0]
 hls_url2 = hls_url1.split('live/')[1]
 hls_url = hls_url2.split('/')[0]
 print (colored('\n => Play URL => {} <=', 'yellow', 'on_blue')).format(hls_url)

 timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
 path = config.get('folders', 'output_folder')
 youtube = config.get('files', 'youtube')
 filename = room + '_C4_' + timestamp + '.ts'
 pf = path + filename
 print (colored('\n => YTDL-REC => {} <=', 'yellow', 'on_red')).format(filename)
 print
 command = ('{} -i --hls-use-mpegts --no-part -q {} -o {}'.format(youtube,hlsurl,pf))
 os.system(command)
 print(colored('\n => END <=', 'yellow','on_blue'))
 sys.exit()

else:
   print (colored('\n => Model ({}) is OFFLINE or ERROR name <=', 'white', 'on_red')).format(model)
   time.sleep(3)
   print(colored('\n => END <=', 'yellow','on_blue'))
   time.sleep(1)
   sys.exit()
