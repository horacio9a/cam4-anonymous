# Cam4 Remote Anonymous FFMPEG Recorder v.1.0.6 by horacio9a for Python 2.7.13

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
print
print(colored(" => START <=", 'yellow', 'on_blue'))
print

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://www.cam4.com/{}'.format(model)
user_agent = {'user-agent': 'Mozilla/5.0 (Android; Mobile; rv:14.0) ..'}
http = urllib3.PoolManager(10, headers=user_agent)
r = http.urlopen('GET',url)
dec = (r.data)
#dec=urllib.unquote(enc).decode()

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

 if "rtmp:" in dec:
  vau0 = dec.split('rtmp://')[1]
  vau = vau0.split('/')[0]

  if len(vau) > 30:
   print(colored(" => TRY AGAIN <=", 'yellow','on_blue'))
   sys.exit()
  else:
   pass

   if len(vau) > 1:
      hlsurl0 = dec.split("hlsUrl: '")[1]
      hlsurl = hlsurl0.split("'")[0]

      vpu0 = dec.split('videoPlayUrl":"')[1]
      vpu = vpu0.split('"')[0]

      model0 = vpu.split('-')[0]

      swf0 = dec.split('playerUrl":"')[1]
      swf = swf0.split('"')[0]

      print (colored(' => App URL => {} <=', 'yellow', 'on_blue')).format(vau)
      print
      print (colored(' => Play URL => {} <=', 'yellow', 'on_blue')).format(vpu)
      print

      timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
      stime = str(time.strftime("%H:%M:%S"))
      path = config.get('folders', 'output_folder')
      filename = model0 + '_C4_' + timestamp
      ffmpeg = config.get('files', 'ffmpeg')
      fn = filename + '.flv'
      pf = (path + fn)
      print (colored(' => FFMPEG-REC => {} <=', 'yellow', 'on_red')).format(fn)
      print
      command = ('{} -loglevel panic -i "{}" -c:v copy -c:a aac -b:a 160k "{}"'.format(ffmpeg,hlsurl,pf))
      os.system(command)
      print(colored(" => END <=", 'yellow','on_blue'))
      sys.exit()

   else:
      print(colored(" => Model in PRIVATE or AWAY ", 'yellow','on_red'))
      print
      print(colored(" => END <=", 'yellow','on_blue'))
      sys.exit()

 else:
   print(colored(" => Model is OFFLINE <=", 'yellow','on_red'))
   print
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()

else:
   print(colored(" => Page Not Found <=", 'yellow','on_red'))
   print
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()
