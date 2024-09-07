import configparser
import os
import sys

class DarkSky:

    def __init__(self):

        if os.path.exists('key.id'):
            self.config = configparser.ConfigParser()
            self.config.read('key.id')
        else:
            print('Missing key.id file')
            sys.exit()

    def getKey(self):
        return self.config['darksky']['key']

    def getLatitude(self):
        return self.config['darksky']['lat']

    def getLongitude(self):
        return self.config['darksky']['lon']

    def getCoordinates(self):
        return (self.getLatitude(), self.getLongitude())

    def getProxies(self):
        try:
            http = self.config['darksky']['http']
            https = self.config['darksky']['https']
        except:
            return None
        
        return {"http": http, "https": https}

    def __str__(self):
        return ('Key: {}; Coordinates: ({}, {})'.format(self.getKey(), self.getLatitude(), self.getLongitude()))

class OpenWeatherMap:    

    def __init__(self):

        if os.path.exists('key.id'):
            self.config = configparser.ConfigParser()
            self.config.read('key.id')
        else:
            print('Missing key.id file')
            sys.exit()

    def getKey(self):
        return self.config['openweathermap']['key']

    def getName(self):
        return self.config['openweathermap']['name']

    def getId(self):
        return self.config['openweathermap']['id']

    def getLatitude(self):
        return self.config['openweathermap']['lat']

    def getLongitude(self):
        return self.config['openweathermap']['lon']

    def getCoordinates(self):
        return (self.getLatitude(), self.getLongitude())

    def __str__(self):
        return ('Name: {}; Id: {}; Key: {}; Coordinates: ({}, {})'.format(self.getName(), self.getId(), self.getKey(), self.getLatitude(), self.getLongitude()))

