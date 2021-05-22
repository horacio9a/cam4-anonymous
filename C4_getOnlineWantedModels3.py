# Cam4 Anonymous Get Online Wanted Models v.2.0.0 by horacio9a for Python 3.9.1
# coding: utf-8

import sys, os, urllib, ssl, re, json, configparser, requests
from sys import exit
Config = configparser.ConfigParser()

setting = {}

def readConfig():
    global setting
    Config.read('config.ini')
    setting = {'wanted_model_list': Config.get('files', 'wanted_model_list')}

offline = False

def getOnlineModels(page):
    attempt = 1
    while attempt < 3:
        try:
            result = urllib.request.urlopen("https://www.cam4.com/directoryCams?directoryJson=true&online=true&url=true&page={}".format(page))
            result = result.read()
            results = json.loads(result.decode())
            return results
        except:
            attempt = attempt + 1

if __name__ == '__main__':
    while True:
        readConfig()
        wanted_model_list = []
        attempt = 1
        with open(setting['wanted_model_list']) as f:
            for model in f:
                models = model.split()
                for theModel in models:
                    wanted_model_list.append(theModel.lower())
        online = []
        while not offline:
            results = getOnlineModels(attempt)
            if len(results['users']) > 1:
                online.extend([user['username'].lower() for user in results['users']])
            else:
                offline = True
            attempt = attempt + 1
        offline = False
        for model in list(set(set(online)).intersection(set(wanted_model_list))):
            online_model_list = online
            for online_wanted_model_list in online_model_list:
                if online_wanted_model_list in wanted_model_list:
                    print(online_wanted_model_list)
        if attempt > 3:
            exit(0)
