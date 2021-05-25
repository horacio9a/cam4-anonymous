# Cam4 Anonymous All Modes Recorder v.2.0.1 by horacio9a for Python 2.7.18
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

init()
print
print(colored(' => START <=', 'white', 'on_blue'))
print

while True:
   try:
      mode = int(raw_input(colored(' => Select => C4_Online_All(2) - C4_Online_Wanted(1) - C4_Wanted(0) => ', 'white', 'on_blue')))
      print
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
           print ' =>',(num+1),value[:-1]
        print
        mn = int(raw_input(colored(' => Select C4 Wanted Model => ', 'white', 'on_blue')))
        print
        nr_lines = sum(1 for line in open(Config.get('files', 'wanted_model_list')))
        if mn > nr_lines:
           print(colored(' => Too big number <=', 'white', 'on_red'))
           print
           print(colored(' => END <=', 'white','on_blue'))
           sys.exit()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  model = open(Config.get('files', 'wanted_model_list'), 'r').readlines()[mn-1][:-1]
  print (colored(' => Selected C4 Wanted Model => {} <=', 'white', 'on_blue')).format(model)
  print

if mod == 'C4OW':
  while True:
     try:
        modellist = open(Config.get('files', 'online_wanted_model_list'),'r')
        for (num,value) in enumerate(modellist):
           print ' =>',(num+1),value[:-1]
        print
        mn = int(raw_input(colored(' => Select C4 Online Wanted Model => ', 'white', 'on_blue')))
        print
        nr_lines = sum(1 for line in open(Config.get('files', 'online_wanted_model_list')))
        if mn > nr_lines:
           print(colored(' => Too big number <=', 'white', 'on_red'))
           print
           print(colored(' => END <=', 'white','on_blue'))
           sys.exit()
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  model = open(Config.get('files', 'online_wanted_model_list'), 'r').readlines()[mn-1][:-1]
  print (colored(' => Selected C4 Online Wanted Model => {} <=', 'white', 'on_blue')).format(model)
  print

if mod == 'C4OA':
  while True:
     try:
        c4oa = int(raw_input(colored(' => Select => <500(0) <1000(1) <1500(2) <2000(3) <2500(4) <3000(5) <3500(6) => ', 'white', 'on_blue')))
        print
        break
     except ValueError:
        print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
  if c4oa > 6:
     sys.exit()
  if c4oa == 0:
     oa = 'OA500'
  if c4oa == 1:
     oa = 'OA1000'
  if c4oa == 2:
     oa = 'OA1500'
  if c4oa == 3:
     oa = 'OA2000'
  if c4oa == 4:
     oa = 'OA2500'
  if c4oa == 5:
     oa = 'OA3000'
  if c4oa == 6:
     oa = 'OA3500'

  if oa == 'OA500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (500, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select C4 Online All Models => ', 'white', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print (colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model)
    print

  if oa == 'OA1000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (1000, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select C4 Online All Model => ', 'white', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print (colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model)
    print

  if oa == 'OA1500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (1500, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select C4 Online All Model => ', 'white', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print (colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model)
    print

  if oa == 'OA2000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (2000, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select C4 Online All Model => ', 'white', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print (colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model)
    print

  if oa == 'OA2500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (2500, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select C4 Online All Model => ', 'white', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print (colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model)
    print

  if oa == 'OA3000':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (3000, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select C4 Online All Model => ', 'white', 'on_blue')))
          print
          nr_lines = sum(1 for line in open(Config.get('files', 'online_all_model_list')))
          if mn > nr_lines:
             print(colored(' => Too big number <=', 'white', 'on_red'))
             print
             print(colored(' => END <=', 'white','on_blue'))
             sys.exit()
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print (colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model)
    print

  if oa == 'OA3500':
    while True:
       try:
          modellist = open(Config.get('files', 'online_all_model_list'),'r')
          for (num, value) in enumerate(modellist):
            if num in range (3500, 5000):
              break
            print ' =>',(num+1),value[:-1]
          print
          mn = int(raw_input(colored(' => Select C4 Online All Model => ', 'white', 'on_blue')))
          print
          break
       except ValueError:
          print(colored('\n => Input must be a number <=\n', 'white', 'on_red'))
    model = open(Config.get('files', 'online_all_model_list'), 'r').readlines()[mn-1][:-1]
    print (colored(' => Selected C4 Online All Model => {} <=', 'white', 'on_blue')).format(model)
    print
	
url ='https://www.cam4.com/rest/v1.0/profile/{}/streamInfo'.format(model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = (r.data)
dec=urllib.unquote(enc)

if 'canUseCDN":true' in dec:
    hlsurl0 = dec.split('cdnURL":"')[1]
    hlsurl = hlsurl0.split('"')[0]
    if len(hlsurl) > 0:
      try:
        streamName0 = dec.split('streamName":"')[1]
        streamName = streamName0.split('-')[0]
      except:
        sys.exit()

      while True:
         try:
            mode = int(raw_input(colored(' => Mode => Exit(6) - URL(5) - YTDL(4) - LS(3) - SL(2) - FFMPEG(1) - FFPLAY(0) => ', 'white', 'on_green')))
            break
         except ValueError:
            print
            print(colored(' => Input must be a number <=', 'white', 'on_red'))
      if mode > 6:
         print
         print(colored(' => Too big number <=', 'white', 'on_red'))
         mod = 'EXIT'
      if mode == 0:
         mod = 'FFPLAY'
      if mode == 1:
         mod = 'FFMPEG'
      if mode == 2:
         mod = 'SL'
      if mode == 3:
         mod = 'LS'
      if mode == 4:
         mod = 'YTDL'
      if mode == 5:
         mod = 'URL'
      if mode == 6:
         mod = 'EXIT'

      timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
      stime = str(time.strftime('%H:%M:%S'))
      path = Config.get('folders', 'output_folder')
      fn = streamName + '_C4_' + timestamp
      fn1 = streamName + '_C4_' + timestamp + '.flv'
      fn2 = streamName + '_C4_' + timestamp + '.mp4'
      fn3 = streamName + '_C4_' + timestamp + '.ts'
      fn4 = streamName + '_C4_' + timestamp + '.txt'
      pf1 = (path + fn1)
      pf2 = (path + fn2)
      pf3 = (path + fn3)
      pf4 = (path + fn4)
      ffplay = Config.get('files', 'ffplay')
      ffmpeg = Config.get('files', 'ffmpeg')
      youtube = Config.get('files', 'youtube')
      streamlink = Config.get('files', 'streamlink')
      livestreamer = Config.get('files', 'livestreamer')

      if mod == 'FFPLAY':
         print
         print (colored(' => FFPLAY => {} <=', 'white', 'on_magenta')).format(fn)
         command = '{} -loglevel panic -i {} -infbuf -autoexit -x 640 -y 480 -window_title "{} * {}"'.format(ffplay,hlsurl,fn,mn)
         os.system(command)
         while True:
            try:
               prog = int(raw_input(colored(' => Mode => URL(5) - YTDL(4) - LS(3) - SL(2) - FFMPEG(1) - Exit(0) => ', 'white', 'on_green')))
               break
            except ValueError:
               print
               print(colored(' => Input must be a number <=', 'white', 'on_red'))
         if prog > 5:
            print
            print(colored(' => Too big number <=', 'white', 'on_red'))
            mod = 'EXIT'
         if prog == 0:
            mod = 'EXIT'
         if prog == 1:
            mod = 'FFMPEG'
         if prog == 2:
            mod = 'SL'
         if prog == 3:
            mod = 'LS'
         if prog == 4:
            mod = 'YTDL'
         if prog == 5:
            mod = 'URL'

      if mod == 'FFMPEG':
         print
         print (colored(' => FFMPEG-REC => {} <=', 'white', 'on_red')).format(fn1)
         command = ('{} -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 128k {}'.format(ffmpeg,hlsurl,pf1))
         os.system(command)
         sys.exit()

      if mod == 'SL':
         print
         print (colored(' => SL-REC => {}  (  Size  @   Speed   ) <=', 'white', 'on_red')).format(fn2)
         print
         command = ('{} hls://{} best -Q --hls-live-edge 1 --hls-playlist-reload-attempts 9 --hls-segment-threads 3 --hls-segment-timeout 5.0 --hls-timeout 20.0 -o {}'.format(streamlink,hlsurl,pf2))
         os.system(command)
         print
         print(colored(' => END <= ', 'white','on_blue'))
         sys.exit()

      if mod == 'LS':
         print
         print (colored(' => LS-REC => {}  (  Size  @   Speed   ) <=', 'white', 'on_red')).format(fn2)
         print
         command = ('{} hlsvariant://{} best -Q -o {}'.format(livestreamer,hlsurl,pf2))
         os.system(command)
         print
         print(colored(' => END <= ', 'white','on_blue'))
         sys.exit()

      if mod == 'YTDL':
         print
         print (colored(' => YTDL-REC => {} <=', 'white', 'on_red')).format(fn3)
         command = ('{} -i --geo-bypass --hls-use-mpegts --no-part -q --no-warnings --no-check-certificate {} -o {}'.format(youtube,hlsurl,pf3))
         os.system(command)
         print
         print(colored(' => END <= ', 'white','on_blue'))
         sys.exit()

      if mod == 'URL':
         print
         print (colored(' => URL => {} <=', 'white', 'on_green')).format(fn4)
         file=open(pf4,'w')
         file.write(hlsurl)
         file.close()
         print
         print(colored(' => END <=', 'white','on_blue'))
         sys.exit()

      if mod == 'EXIT':
         print
         print(colored(' => END <=', 'white','on_blue'))
         sys.exit()

    else:
      sys.exit()

else:
   print(colored(' => Model is offline or wrong name <=', 'white','on_red'))
   print
   print(colored(' => END <=', 'white','on_blue'))
   sys.exit()
