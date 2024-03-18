# Cam4 FFMPEG/STREAMLINK/YTDL Anonymous All Modes Recorder v.2.1.0 by horacio9a for Python 3.12.2
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, requests, command, streamlink
urllib3.disable_warnings()
from urllib3 import PoolManager
from urllib.parse import quote
from urllib.parse import unquote
from colorama import init, Fore, Back, Style
from termcolor import colored
import configparser
Config = configparser.ConfigParser()
Config.read('config3.ini')
country_domain = Config.get('settings', 'country_domain')

init()
print()
print(colored(' => START <=', 'white', 'on_blue'))
print()

while True:
   try:
      mode = int(input(colored(' => Select => C4_Online_All(2) - C4_Online_Wanted(1) - C4_Wanted(0) => ', 'white', 'on_blue')))
      print()
      break
   except ValueError:
      print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
if mode > 2:
   print(colored(' => Too big number <=', 'white', 'on_red'))
   sys.exit()
if mode == 0:
   mod = 'C4W'
if mode == 1:
   mod = 'C4OW'
if mode == 2:
   mod = 'C4OA'

if mod == 'C4W':
  while True:
     try:
        modellist = open(Config.get('files', 'wanted_model_list'),'r')
        for (num,value) in enumerate(modellist):
           print(' =>',(num+1),value[:-1])
        print()
        mn = int(input(colored(' => Select C4 Wanted Model => ', 'white', 'on_blue')))
        print()
        nr_lines = sum(1 for line in open(Config.get('files', 'wanted_model_list')))
        if mn > nr_lines:
           print(colored(' => Too big number <=', 'white', 'on_red'))
           print()
           print(colored(' => END <=', 'white','on_blue'))
           sys.exit()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  model = open(Config.get('files', 'wanted_model_list'), 'r').readlines()[mn-1][:-1]
  print ((colored(' => Selected C4 Wanted Model => {} <=', 'white', 'on_blue')).format(model))
  print()

if mod == 'C4OW':
  while True:
     try:
        modellist = open(Config.get('files', 'online_wanted_model_list'),'r')
        for (num,value) in enumerate(modellist):
           print(' =>',(num+1),value[:-1])
        print()
        mn = int(input(colored(' => Select C4 Online Wanted Model => ', 'white', 'on_blue')))
        print()
        nr_lines = sum(1 for line in open(Config.get('files', 'online_wanted_model_list')))
        if mn > nr_lines:
           print(colored(' => Too big number <=', 'white', 'on_red'))
           print()
           print(colored(' => END <=', 'white','on_blue'))
           sys.exit()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  model = open(Config.get('files', 'online_wanted_model_list'), 'r').readlines()[mn-1][:-1]
  print ((colored(' => Selected C4 Online Wanted Model => {} <=', 'white', 'on_blue')).format(model))
  print()

if mod == 'C4OA':
  while True:
     try:
        c4oa = int(input(colored(' => Select => <250(0) <500(1) <750(2) <1000(3) <1250(4) <1500(5) <1750(6) <2000(7) <2250(8) <2500(9) <2750(10) <3000(11) => ', 'white', 'on_blue')))
        print()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  if c4oa > 11:
     sys.exit()
  if c4oa == 0:
     oa = 'OA250'
  if c4oa == 1:
     oa = 'OA500'
  if c4oa == 2:
     oa = 'OA750'
  if c4oa == 3:
     oa = 'OA1000'
  if c4oa == 4:
     oa = 'OA1250'
  if c4oa == 5:
     oa = 'OA1500'
  if c4oa == 6:
     oa = 'OA1750'
  if c4oa == 7:
     oa = 'OA2000'
  if c4oa == 8:
     oa = 'OA2250'
  if c4oa == 9:
     oa = 'OA2500'
  if c4oa == 10:
     oa = 'OA2750'
  if c4oa == 11:
     oa = 'OA3000'

  if oa == 'OA250':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (250, 3000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (500, 3000):
              break
            print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA750':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (750, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA1000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (1000, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA1250':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (1250, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA1500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (1500, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA1750':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (1750, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA2000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (2000, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA2250':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (2250, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()

  if oa == 'OA2500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (2500, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()
	
  if oa == 'OA2750':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (2750, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()
	
  if oa == 'OA3000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
             if num in range (3000, 3000):
                break
             print(' =>',(num+1),value[:-1])
          print()
          mn = int(input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print()
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print()
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print ((colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model))
    print()
	
url ='https://{}.cam4.com/rest/v1.0/profile/{}/streamInfo'.format(country_domain, model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = quote(r.data)
dec= unquote(enc)

if len(dec) > 0:
    hlsur2 = dec.split('cdnURL":"')[1]
    hlsurl = hlsur2.split('"')[0]
    print ((colored(' => HlsUrl => {} <=', 'white', 'on_magenta')).format(hlsurl))
    print ()
    try:
       mode = int(input(colored(' => Mode => Exit(5) - URL(4) - YTDL(3) - SL(2) - FFMPEG(1) - PLAYER(0) => ', 'white', 'on_green')))
    except ValueError:
       print()
       print(colored(' => Input must be a number <=', 'white', 'on_red'))
    if mode > 5:
       print()
       print(colored(' => Too big number <=', 'white', 'on_red'))
       mod = 'EXIT'
    if mode == 0:
       mod = 'PLAYER'
    if mode == 1:
       mod = 'FFMPEG'
    if mode == 2:
       mod = 'SL'
    if mode == 3:
       mod = 'YTDL'
    if mode == 4:
       mod = 'URL'
    if mode == 5:
       mod = 'EXIT'

    timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
    path = Config.get('folders', 'output_folder')
    fn = model + '_C4_' + timestamp
    fn1 = model + '_C4_' + timestamp + '.flv'
    fn2 = model + '_C4_' + timestamp + '.mp4'
    fn3 = model + '_C4_' + timestamp + '.ts'
    fn4 = model + '_C4_' + timestamp + '.txt'
    pf1 = (path + fn1)
    pf2 = (path + fn2)
    pf3 = (path + fn3)
    pf4 = (path + fn4)
    player = Config.get('files', 'player')
    ffmpeg = Config.get('files', 'ffmpeg')
    youtube = Config.get('files', 'youtube')
    streamlink = Config.get('files', 'streamlink')

    if mod == 'PLAYER':
       print()
       print ((colored(' => PLAYER => {} <=', 'white', 'on_magenta')).format(fn))
       print()
       command = ('{} -p {} {} best'.format(streamlink, player, hlsurl))
       os.system(command)
       while True:
          try:
             print()
             prog = int(input(colored(' => Mode => URL(4) - YTDL(3) - SL(2) - FFMPEG(1) - Exit(0) => ', 'white', 'on_green')))
             break
          except ValueError:
             print()
             print(colored(' => Input must be a number <=', 'white', 'on_red'))
             print()
       if prog > 4: 
          print()
          print(colored(' => Too big number <=', 'white', 'on_red'))
          mod = 'EXIT'
       if prog == 0:
          mod = 'EXIT'
       if prog == 1:
          mod = 'FFMPEG'
       if prog == 2:
          mod = 'SL'
       if prog == 3:
          mod = 'YTDL'
       if prog == 4:
          mod = 'URL'

    if mod == 'FFMPEG':
       print()
       print ((colored(' => FFMPEG-REC => {} <=', 'white', 'on_red')).format(pf1))
       command = '{} -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 128k {}'.format(ffmpeg,hlsurl,pf1)
       os.system(command)
       sys.exit()

    if mod == 'SL':
       print()
       print ((colored(' => SL-REC => {}  Size    ( Time @   Speed   ) <=', 'white', 'on_red')).format(pf2))
       print()
       command = ('{} hls://{} best -Q --hls-live-edge 1 --hls-playlist-reload-attempts 9 --hls-segment-threads 3 --hls-segment-timeout 5.0 --hls-timeout 20.0 -o {}'.format(streamlink,hlsurl,pf2))
       os.system(command)
       print()
       print(colored(' => END <=', 'white','on_blue'))
       sys.exit()

    if mod == 'YTDL':
       print()
       print ((colored(' => YTDL-REC => {} <=', 'white', 'on_red')).format(pf3))
       command = ('{} -i --geo-bypass --hls-use-mpegts --no-part -q --no-warnings --no-check-certificate {} -o {}'.format(youtube,hlsurl,pf3))
       os.system(command)
       print()
       print(colored(' => END <= ', 'white','on_blue'))
       sys.exit()

    if mod == 'URL':
       print()
       print((colored(' => URL => {} <=', 'white', 'on_red')).format(pf4))
       file=open(pf4,'w')
       file.write(hlsurl)
       file.close()
       print()
       print(colored(' => END <=', 'white','on_blue'))
       sys.exit()

    if mod == 'EXIT':
       print()
       print(colored(' => END <=', 'white','on_blue'))
       sys.exit()

else:
   print(colored(' => Model is offline or wrong name <=', 'white','on_red'))
   print()
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()
