# Cam4 Anonymous Get Online All Models v.2.0.0 by horacio9a for Python 3.9.1
# coding: utf-8

import sys, os, urllib, ssl, re, json, gevent, requests
from sys import exit
offline = False

def getOnlineUsers(page):
    attempt = 1
    while attempt <= 3:
        try:
            timeout = gevent.Timeout(8)
            timeout.start()
            result = urllib.request.urlopen("https://www.cam4.com/directoryCams?directoryJson=true&online=true&url=true&page={}".format(page))
            result = result.read()
            results = json.loads(result.decode())
            return results
        except gevent.Timeout:
            attempt = attempt + 1
            if attempt > 1:
                exit(0)
			
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
            online_all_model_list = username.lower()
            print(online_all_model_list)
        if attempt > 3:
            exit(0)
