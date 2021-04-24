# Cam4 Anonymous All Modes Recorder v.1.1.1 by horacio9a for Python 3.9.1
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
print()


while True:
   try:
      modellist = open(config.get('files', 'model_list'),'r')
      for (num,value) in enumerate(modellist):
         print(' =>',(num+1),value[:-1])
      print()
      mn = int(input(' => Select C4 Model => '))
      break
   except ValueError:
      print(colored('\n => Input must be a number <=', 'white', 'on_red'))
      print()
model = open(config.get('files', 'model_list'), 'r').readlines()[mn-1][:-1]

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

    hlsurl = 'https://cam4-hls.xcdnpro.com/{}/cam4-origin-live/{}_aac/playlist.m3u8'.format(wcdn,vpu)
 
    print ((colored('\n => Room: ({}) * Member since: ({}) * Room status: ({}) <=', 'white', 'on_blue')).format(room,ms,status))
    print ((colored('\n => Age: ({}) * Gender: ({}) * Orientation: ({}) * Status: ({}) <=', 'white', 'on_blue')).format(age,gender,orientation,sta))
    print ((colored('\n => Country: ({}) * Location: ({}) * Ethnic: ({}) <=', 'white', 'on_blue')).format(country,loc,eth))
 
    while True:
       try:
          print()
          mode = int(input(' => Mode => Exit(6)  URL(5)  YTDL(4)  SL(3)  FFMPEG(2)  RTMP(1)  FFPLAY(0) => '))
          break
       except ValueError:
          print()
          print(colored(' => Input must be a number <=', 'white', 'on_red'))
    if mode > 6:
       print()
       print(colored(' => Too big number <=', 'white', 'on_red'))
       mod = 'EXIT'
    if mode == 0:
       mod = 'FFPLAY'
    if mode == 1:
       mod = 'RTMP'
    if mode == 2:
       mod = 'FFMPEG'
    if mode == 3:
       mod = 'SL'
    if mode == 4:
       mod = 'YTDL'
    if mode == 5:
       mod = 'URL'
    if mode == 6:
       mod = 'EXIT'

    timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
    stime = str(time.strftime('%H:%M:%S'))
    path = config.get('folders', 'output_folder')
    fn = room + '_C4_' + timestamp
    fn1 = room + '_C4_' + timestamp + '.flv'
    fn2 = room + '_C4_' + timestamp + '.mp4'
    fn3 = room + '_C4_' + timestamp + '.ts'
    fn4 = room + '_C4_' + timestamp + '.txt'
    pf1 = (path + fn1)
    pf2 = (path + fn2)
    pf3 = (path + fn3)
    pf4 = (path + fn4)
    rtmp = config.get('files', 'rtmpdump')
    ffplay = config.get('files', 'ffplay')
    ffmpeg = config.get('files', 'ffmpeg')
    youtube = config.get('files', 'youtube')
    streamlink = config.get('files', 'streamlink')

    if mod == 'FFPLAY':
       print ((colored('\n => FFPLAY => {} <=', 'white', 'on_magenta')).format(fn))
       command = '{} -loglevel panic -i {} -infbuf -autoexit -x 640 -y 480 -window_title "{} * {}"'.format(ffplay,hlsurl,fn,mn)
       os.system(command)
       while True:
          try:
             prog = int(input(' => Mode => URL(5) => YTDL(4) => SL(3) => FFMPEG(2) => RTMP(1) => Exit(0) => '))
             break
          except ValueError:
             print()
             print(colored(' => Input must be a number <=', 'white', 'on_red'))
       if prog > 5:
          print()
          print(colored(' => Too big number <=', 'white', 'on_red'))
          mod = 'EXIT'
       if prog == 0:
          mod = 'EXIT'
       if prog == 1:
          mod = 'RTMP'
       if prog == 2:
          mod = 'FFMPEG'
       if prog == 3:
          mod = 'SL'
       if prog == 4:
          mod = 'YTDL'
       if prog == 5:
          mod = 'URL'

    if mod == 'RTMP':
       print ((colored('\n => RTMP-REC => {} <=', 'white', 'on_red')).format(fn1))
       command = '{} -r"rtmp://{}/cam4-edge-live" -a"cam4-edge-live" -W"{}" --live -y"{}" -o"{}" -q'.format(rtmp,vau,swf,vpu,pf1)
       os.system(command)
       sys.exit()

    if mod == 'FFMPEG':
       print ((colored('\n => FFMPEG-REC => {} <=', 'white', 'on_red')).format(fn1))
       command = ('{} -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 128k {}'.format(ffmpeg,hlsurl,pf1))
       os.system(command)
       sys.exit()

    if mod == 'SL':
       print ((colored('\n => SL-REC => {} ', 'white', 'on_red')).format(fn2))
       command = ('{} hls://{} best -Q --hls-live-edge 1 --hls-playlist-reload-attempts 9 --hls-segment-threads 3 --hls-segment-timeout 5.0 --hls-timeout 20.0 -o {}'.format(streamlink,hlsurl,pf2))
       os.system(command)
       sys.exit()

    if mod == 'YTDL':
       print ((colored('\n => YTDL-REC => {} <=', 'white', 'on_red')).format(fn3))
       command = ('{} -i --geo-bypass --hls-use-mpegts --no-part -q --no-warnings --no-check-certificate {} -o {}'.format(youtube,hlsurl,pf3))
       os.system(command)
       sys.exit()

    if mod == 'URL':
       print ((colored('\n => URL => {} <=', 'white', 'on_green')).format(fn4))
       file=open(pf4,'wb')
       file.write(hlsurl)
       file.close()
       raw_input(colored('\n => Press Enter to exit <=', 'white', 'on_blue'))
       sys.exit()

    if mod == 'EXIT':
       print(colored('\n => END <=', 'white','on_blue'))
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
