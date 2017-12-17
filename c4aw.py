# Cam4 Anonymous All Modes Full Windows Recorder v.1.0.7 by horacio9a for Python 2.7.13

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
user_agent = {'user-agent': 'Mozilla/5.0 (Android; Mobile; rv:14.0) ..'}
http = urllib3.PoolManager(10, headers=user_agent)
r = http.urlopen('GET',url)
enc = (r.data)
dec=urllib.unquote(enc).decode()

state0 = dec.split("showState: '")[1]
state = state0.split("'")[0]

if len(state) == 0:
   print(colored(" => Model is OFFLINE or wrong name<=", 'yellow','on_blue'))
   print
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()
else:
   pass

print (colored(' => Model State => {} <=', 'white', 'on_green')).format(state)
print

if len(state) > 0:
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

 vau0 = dec.split('rtmp://')[1]
 vau = vau0.split('/')[0]

 if len(vau) > 30:
    print(colored(" => TRY AGAIN <=", 'yellow','on_blue'))
    sys.exit()
 else:
    pass

 if len(vau) > 1:
   vpu0 = dec.split('videoPlayUrl":"')[1]
   vpu = vpu0.split('"')[0]

   rname = vpu.split('-')[0]
   lwcdn = vpu.split('-')[1]

   hlsurl1 = 'https://lwcdn-{}.cam4.com/cam4-origin-live/ngrp:{}_all/playlist.m3u8'.format(lwcdn,vpu)
   hlsurl2 = 'https://lwcdn-{}.cam4.com/cam4-origin-live/amlst:{}_aac/playlist.m3u8'.format(lwcdn,vpu)
   hlsurl = 'https://lwcdn-{}.cam4.com/cam4-origin-live/{}_aac/playlist.m3u8'.format(lwcdn,vpu)
   hlsurl0 = dec.split("hlsUrl: '")[1]
#   hlsurl = hlsurl0.split("'")[0]
   purl0 = hlsurl.split('live/')[1]
   purl = purl0.split('/')[0]
   print (colored(' => Play URL => {} <=', 'yellow', 'on_blue')).format(purl)
   print

   swf0 = dec.split('playerUrl":"')[1]
   swf = swf0.split('"')[0]

   while True:
      try:
         mode = int(raw_input(colored(" => Mode => EXIT(5) SL(4) FFMPEG(3) FFPLAY(2) YTDL(1) RTMP(0) => ", "yellow", "on_blue")))
         print
         break
      except ValueError:
         print(colored("\n => Input must be a number <=", "yellow", "on_red"))
         print
   if mode == 0:
        mod = 'RTMP'
   if mode == 1:
        mod = 'YTDL'
   if mode == 2:
        mod = 'FFPLAY'
   if mode == 3:
        mod = 'FFMPEG'
   if mode == 4:
        mod = 'SL'
   if mode == 5:
        mod = 'EXIT'

timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
stime = str(time.strftime("%H:%M:%S"))
path = config.get('folders', 'output_folder')
filename = rname + '_C4_' + timestamp
rtmp = config.get('files', 'rtmpdump')
ffplay = config.get('files', 'ffplay')
ffmpeg = config.get('files', 'ffmpeg')
youtube = config.get('files', 'youtube')
streamlink = config.get('files', 'streamlink')

if mod == 'RTMP':
   fn = filename + '.flv'
   pf = (path + fn)
   print (colored(' => RTMP-REC => {} <=', 'yellow', 'on_red')).format(fn)
   print
   command = 'start {} -r"rtmp://{}/cam4-edge-live" -a"cam4-edge-live" -W"{}" --live -y"{}" -o"{}"'.format(rtmp,vau,swf,vpu,pf)
   os.system(command)
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()

if mod == 'YTDL':
   fn = filename + '.ts'
   pf = (path + fn)
   print (colored(" => YTDL-REC => {} <=", "yellow", "on_red")).format(fn)
   print
   command = ('start {} -i --hls-use-mpegts --no-part {} -o {}'.format(youtube,hlsurl,pf))
   os.system(command)
   print(colored(" => END <=", "yellow","on_blue"))
   sys.exit()

if mod == 'FFPLAY':
   print (colored(" => FFPLAY => {} <=", "yellow", "on_magenta")).format(filename)
   print
   command = ('start {} -i "{}" -infbuf -autoexit -window_title "{} * {} * {} * {}"'.format(ffplay,hlsurl,rname,loc,stime,mn))
   os.system(command)
   print(colored(" => END <=", "yellow","on_blue"))
   sys.exit()

if mod == 'FFMPEG':
   fn = filename + '.flv'
   pf = (path + fn)
   print (colored(' => FFMPEG-REC => {} <=', 'yellow', 'on_red')).format(fn)
   print
   command = ('start {} -i "{}" -c:v copy -c:a aac -b:a 160k "{}"'.format(ffmpeg,hlsurl,pf))
   os.system(command)
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()

if mod == 'SL':
   fn = filename + '.mp4'
   pf = (path + fn)
   print (colored(' => SL-REC >>> {} <<<', 'yellow', 'on_red')).format(fn)
   print
   command = ('start {} hls://"{}" best -o "{}"'.format(streamlink,hlsurl,pf))
   os.system(command)
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()

if mod == 'EXIT':
   print(colored(" => END <=", 'yellow','on_blue'))
   sys.exit()
