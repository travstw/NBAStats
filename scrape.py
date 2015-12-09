import requests
import json
import pylab


class player():
    def __init__(self, data):
        self.games = data['resultSets'][0]['rowSet'][:]
        
    def threesMadeEachGame(self):
        madeThrees = []
        for game in range(len(self.games)):
            madeThrees.append(self.games[game][10])
        
        return madeThrees
        
    def average(self, dataList):
        
        return sum(dataList)/len(dataList)
        
    def unitDeviation(self, dataList):
        deviationList = []
        ave = self.average(dataList)
        
        for data in range(len(dataList)):
            diff = abs(dataList[data] - ave)
            deviationList.append(diff)
            
        return deviationList
        
        
        
    def printGames(self):
        print self.games
        


def getStats(PlayerID = 201939):
    url = 'http://stats.nba.com/stats/playergamelog?LeagueID=00&PlayerID='+ str(PlayerID) +'&Season=2015-16&SeasonType=Regular+Season'
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    return data
    
    


p = player(getStats())
#print(p.threesMadeEachGame())

pylab.figure(0)
pylab.plot(p.threesMadeEachGame(),'bo')
#pylab.plot(p.unitDeviation(p.threesMadeEachGame()), 'ro')
pylab.title("3 Point Shots Made Each Game")
pylab.xlabel('Games')
pylab.ylabel('3 PFG')
pylab.ylim(0, 10)
pylab.show()
