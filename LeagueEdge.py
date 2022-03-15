# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:37:32 2022

@author: Jake
"""

import requests
import urllib3
urllib3.disable_warnings()

class LeagueEdge():
    def __init__(self, apiKey="RGAPI-f58cdf1b-babe-4eb0-9ff3-98b65ee6ed10", summonerName="RoleplayFountain"):
        self.apiKey = apiKey
        self.summonerName = summonerName
    
    # Web API
    def getServerStatus(self):
        return requests.get("https://na1.api.riotgames.com/lol/status/v4/platform-data?api_key={}".format(self.apiKey))
    
    def getSummonerByName(self):
        return requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(self.summonerName, self.apiKey))
    
        
    def getMatchData(self):
        pass
    
    #Live Client API
    def getAllData(self):
        return requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False)
    
    def getActivePlayer(self):
        return requests.get("https://127.0.0.1:2999/liveclientdata/activeplayer", verify=False)

    def getActivePlayerAbilities(self):
        return requests.get("https://127.0.0.1:2999/liveclientdata/activeplayerabilities", verify=False)
    
    def getActivePlayerRunes(self):
        return requests.get("https://127.0.0.1:2999/liveclientdata/activeplayerrunes", verify=False)
    
    def getAllPlayers(self):
        return requests.get("https://127.0.0.1:2999/liveclientdata/playerlist", verify=False)
    
    def getPlayerScore(self, summonerName):
        return requests.get("https://127.0.0.1:2999/liveclientdata/playerscores?summonerName={}".format(summonerName), verify=False)
    
    def getPlayerSummonerSpells(self, summonerName):
        return requests.get("https://127.0.0.1:2999/liveclientdata/playersummonerspells?summonerName={}".format(summonerName), verify=False)
    
    def getPlayerRunes(self, summonerName):
        return requests.get("https://127.0.0.1:2999/liveclientdata/playermainrunes?summonerName={}".format(summonerName), verify=False)

    def getPlayerItems(self, summonerName):
        return requests.get("https://127.0.0.1:2999/liveclientdata/playeritems?summonerName={}".format(summonerName), verify=False)
    
    def getGameEvents(self):
        return requests.get("https://127.0.0.1:2999/liveclientdata/eventdata", verify=False)
    
    def getGameInfo(self):
        return requests.get("https://127.0.0.1:2999/liveclientdata/gamestats", verify=False)