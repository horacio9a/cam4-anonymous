# Cam4 Anonymous RTMP Recorder v.1.0.4 by horacio9a for Python 2.7.13

import sys, os, urllib, urllib3, ssl, re, time, datetime, command
urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.cfg')

init()
print
print(colored(" => START <=", 'yellow', 'on_blue'))
print

while True:
   try:
      modellist = open(config.get('files', 'model_list'),'r')
      for (num,value) in enumerate(modellist):
         print ' =>',(num+1),value[:-1]
      print
      mn = int(raw_input(colored(" => Select C4 Model => ", 'yellow', 'on_blue')))
      print
      break
   except ValueError:
      print
      print(colored(" => Input must be a number <=", 'yellow', 'on_red'))
      print
model = open(config.get('files', 'model_list'), 'r').readlines()[mn-1][:-1]
print (colored(' => Selected C4 Model => {} <=', 'yellow', 'on_blue')).format(model)
print

url ='https://www.cam4.com/{}'.format(model)
http_pool = urllib3.connection_from_url(url)
r = http_pool.urlopen('GET',url)
enc = (r.data)
dec=urllib.unquote(enc).decode()

if "Trending Cams" not in dec:
 try:
   age0 = dec.split('Age:</')[1]
   age1 = age0.split('</')[0]
   age = age1.split('field">')[1]
 except:
   age = ''

 try:
   loc0 = dec.split('Location:</')[1]
   loc1 = loc0.split('</')[0]
   loc2 = loc1.split('">')[1]
   loc3 = re.sub(',', '', loc2)
   loc = re.sub(' ', '', loc3)
 except:
   loc = ''

 try:
   sta0 = dec.split('Status:</')[1]
   sta1 = sta0.split('</')[0]
   sta = sta1.split('field">')[1]
 except:
   sta = ''

 try:
   occ0 = dec.split('Occupation:</')[1]
   occ1 = occ0.split('</')[0]
   occ = occ1.split('field">')[1]
 except:
   occ = ''

 print (colored(' => Age:{} * Location:{} * Status:{} * Job:{} <=', 'yellow', 'on_blue')).format(age,loc,sta,occ)
 print

 if "cam-offline" in dec:
  vau0 = dec.split('videoAppUrl=')[1]
  vau1 = vau0.split('&')[0]
  vau2 = re.sub('rtmp://', '', vau1)
  vau = re.sub('/cam4-edge-live', '', vau2)

  if len(vau) > 20:
   print(colored(" => TRY AGAIN <=", 'yellow','on_blue'))
   sys.exit()
  else:
   pass

   if len(vau) > 1:
      vpu0 = dec.split('videoPlayUrl=')[1]
      vpu = vpu0.split('&')[0]

      model0 = vpu.split('-')[0]

      swf0 = dec.split('data="')[1]
      swf = swf0.split('"')[0]

      print (colored(' => App URL => {} <=', 'white', 'on_blue')).format(vau)
      print
      print (colored(' => Play URL => {} <=', 'white', 'on_blue')).format(vpu)
      print

      timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
      path = config.get('folders', 'output_folder')
      filename = model0 + '_C4_' + timestamp + '.flv'
      pf = (path + filename)
      rtmp = config.get('files', 'rtmpdump')

      print (colored(' => REC => {} <=', 'yellow', 'on_red')).format(filename)
      command = 'start {} -r"{}" -a"cam4-edge-live" -W"{}" --live -y"{}" -o"{}"'.format(rtmp,vau1,swf,vpu,pf)
      os.system(command)
      print
      time.sleep(1)    # pause 1 second
      print(colored(" => END <=", 'yellow','on_blue'))
      sys.exit()

   else:
      print(colored(" => Model in PRIVATE or AWAY ", 'yellow','on_red'))
      print
      time.sleep(1)    # pause 1 second
      print(colored(" => END <=", 'yellow','on_blue'))
      sys.exit()

 else:
   print(colored(" => Model is OFFLINE <=", 'yellow','on_red'))
   print
   time.sleep(1)    # pause 1 second
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()

else:
   print(colored(" => Page Not Found <=", 'yellow','on_red'))
   print
   time.sleep(1)    # pause 1 second
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()
