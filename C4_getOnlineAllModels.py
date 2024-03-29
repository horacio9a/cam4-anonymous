# Cam4 Anonymous Get Online All Models v.2.1.0 by horacio9a for Python 2.7.18
# coding: utf-8

import sys, os, urllib, ssl, re, json, requests
offline = False
import configparser
Config = configparser.ConfigParser()
Config.read('config.ini')
country_domain = Config.get('settings', 'country_domain')

def getOnlineUsers(page):
   attempt = 1
   while attempt < 3:
      try:
         results = requests.get("https://{}.cam4.com/directoryCams?directoryJson=true&online=true&url=true&page={}".format(country_domain, page)).json()
         return results
      except:
         attempt = attempt + 1

if __name__ == '__main__':
   while True:
      attempt = 1
      online = []
      while not offline:
         results = getOnlineUsers(attempt)
         if len(results['users']) > 1:
            online.extend([user['username'] for user in results['users']])
         else:
            offline = True
         attempt = attempt + 1
      offline = False
      for username in online:
         online_all_model_list = username
         print(online_all_model_list)
      if attempt > 3:
         sys.exit()
