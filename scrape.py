import requests
import json
import pylab


class player():
    def __init__(self, games, shots):
        self.games = games['resultSets'][0]['rowSet'][:]
        self.shots = shots['resultSets'][0]['rowSet'][:]
        
    def threesMadeEachGame(self):
        madeThrees = []
        for game in range(len(self.games)):
            madeThrees.append(self.games[game][10])
        
        return madeThrees
        
    def shotDistanceAll(self):
        shotDist = []
        
        for shot in range(len(self.shots)):
            shotDist.append(self.shots[shot][11])
            
        return shotDist
        
    def shotsMadeDistance(self):
        shotsMade = []
        
        for shot in range(len(self.shots)):
            if self.shots[shot][13] == 'made':
                shotsMade.append(self.shots[shot][11])
                
        return shotsMade
        
    def shotsMissedDistance(self):
        shotsMissed = []
        
        for shot in range(len(self.shots)):
            if self.shots[shot][13] == 'missed':
                shotsMissed.append(self.shots[shot][11])
                
        return shotsMissed
        
        
        
    def shotDefDistAll(self):
        defDist = []
        
        for shot in range(len(self.shots)):
            defDist.append(self.shots[shot][16])
            
        return defDist
        
    def shotDefDistMade(self):
        defDistMade = []
        
        for shot in range(len(self.shots)):
            if self.shots[shot][13] == 'made':
                defDistMade.append(self.shots[shot][16])
            
        return defDistMade
    
    def shotDefDistMissed(self):
        defDistMissed = []
        
        for shot in range(len(self.shots)):
            if self.shots[shot][13] == 'missed':
                defDistMissed.append(self.shots[shot][16])
            
        return defDistMissed
        
        
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
    
def getShotStats(PlayerID = 201939):
    url = 'http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID=201939&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    return data
    


p = player(getStats(), getShotStats())


#pylab.figure(0)
#pylab.plot(p.shotDefDistMade(),'go')
#pylab.plot(p.shotDefDistMissed(), 'ro')
#
#pylab.title("Defender Distance")
#pylab.xlabel('Shots')
#pylab.ylabel('Distance')
##pylab.ylim(0, 10)
#pylab.show(0)

pylab.figure(1)
pylab.hist(p.shotDefDistMade())
pylab.xlabel('Defender Distance')
pylab.ylabel('Shots Made')
pylab.show(1)

pylab.figure(2)
pylab.hist(p.shotDefDistMissed(), color = 'red')
pylab.xlabel('Defender Distance')
pylab.ylabel('Shots Missed')
pylab.show(2)
