# Cam4 Remote Anonymous RTMP Recorder v.1.1.1 by horacio9a for Python 2.7.18
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, command
urllib3.disable_warnings()
from urllib3 import PoolManager
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.ini')

init()
print(colored('\n => START <=', 'white', 'on_blue'))

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://www.cam4.com/{}'.format(model)
user_agent = {'user-agent': 'Mozilla/5.0 (Android; Mobile; rv:14.0) ..'}
http = urllib3.PoolManager(10, headers=user_agent)
r = http.urlopen('GET',url)
enc = (r.data)
dec=urllib.unquote(enc).decode()

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

    vau0 = dec.split('rtmp://')[1]
    vau = vau0.split('/')[0]

    if len(vau) > 30:
       print(colored("\n => TRY AGAIN <=", 'white','on_blue'))
       time.sleep(3)
       print(colored('\n => END <=', 'white','on_blue'))
       time.sleep(1)
       sys.exit()
    else:
       pass

    vpu0 = dec.split('videoPlayUrl":"')[1]
    vpu = vpu0.split('"')[0]

    wcdn = vpu.split('-')[1]

    swf0 = dec.split('playerUrl":"')[1]
    swf = swf0.split('"')[0]

    print (colored('\n => Room: ({}) * Member since: ({}) * Room status: ({}) <=', 'white', 'on_blue')).format(room,ms,status)
    print (colored('\n => Age: ({}) * Gender: ({}) * Orientation: ({}) * Status: ({}) <=', 'white', 'on_blue')).format(age,gender,orientation,sta)
    print (colored('\n => Country: ({}) * Location: ({}) * Ethnic: ({}) <=', 'white', 'on_blue')).format(country,loc,eth)
 
    timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
    path = config.get('folders', 'output_folder')
    filename = room + '_C4_' + timestamp
    rtmp = config.get('files', 'rtmpdump')
    filename = room + '_C4_' + timestamp + '.flv'
    pf = path + filename
    print (colored('\n => RTMP-REC => {} <=', 'white', 'on_red')).format(filename)
    print
    command = '{} -r"rtmp://{}/cam4-edge-live" -a"cam4-edge-live" -W"{}" --live -y"{}" -o"{}" -q'.format(rtmp,vau,swf,vpu,pf)
    os.system(command)
    sys.exit()

  else:
    print(colored('\n => Model is offline <=', 'white','on_red'))
    print
    print(colored(' => END <=', 'white','on_blue'))
    sys.exit()

else:
   print(colored('\n => Page Not Found <=', 'white','on_red'))
   print
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()