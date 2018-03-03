# -*- coding: utf-8 -*-

import json
from objects import *

configfile = "parameters.json"

class ConfigManager(object):
    def __init__(self):
        self.config = None

    def readConfig(self):
        self.configfile = configfile
        cfgf = open(self.configfile,'r')
        cfg = cfgf.read()
        try:
            self.config = json.loads(cfg)
        except:
            print ('Reading config file error')
class Map(object):
    def __ini__(self):
        pass
        self.map = None
        self.mapName = None
        self.fileName = None
        self.blox = []
        self.enemies = []
        self.player = []
        self.doors = []
        self.background = None
    def load(self, mapFile):
        mapf = open(mapFile,'r')
        map = mapf.read()
        try:
            self.map = json.load(map)
            self.fileName = mapFile
        except:
            print ("Reading map error")
        map.close()
    def parse(self):
        if self.map:
            # blocks objects
            self.mapName = self.map['MapName']
            objects = self.map['Objects']
            for o in self.map.keys():
                if o['Type'] == 'Block':
                    try:
                        obj = compile(o['Class'],'<string>','single')
                        obj.Xpos(o['Xpos'])
                        obj.Ypos(o['Ypos'])                        
                        self.blox.append(obj)
                    except:
                        raise
                elif o['Type'] == 'Enemy':
                    try:
                        obj = compile(o['Class'],'<string>','single')
                        obj.Xpos(o['Xpos'])
                        obj.Ypos(o['Ypos'])                        
                        self.enemies.append(obj)
                    except:
                        raise
                elif o['Type'] == 'Door':
                    try:
                        obj = compile(o['Class'],'<string>','single')
                        obj.Xpos(o['Xpos'])
                        obj.Ypos(o['Ypos'])                        
                        self.doors.append(obj)
                    except:
                        raise
        else:
            print ("Nothing to parse")
    def write(self):
        if self.mapName:
            fle = open(self.fileName,'w')
        else:
            print ("no map loaded")