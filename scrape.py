import requests
import json
import pylab


class player():
    def __init__(self, games, shots, shots2):
        self.games = games['resultSets'][0]['rowSet'][:]
        self.shots = shots['resultSets'][0]['rowSet'][:]
        self.shots2 = shots2['resultSets'][0]['rowSet'][:]
        
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
        
    
    def shotLocations(self):
        shotsMadeX = []
        shotsMadeY = []
        shotsMissedX = []
        shotsMissedY = []
        
        for shot in range(len(self.shots2)):
            if self.shots2[shot][20] == 1:
                shotsMadeX.append(self.shots2[shot][17])
                shotsMadeY.append(self.shots2[shot][18])
            else:
                shotsMissedX.append(self.shots2[shot][17])
                shotsMissedY.append(self.shots2[shot][18]) 
        
        
        return [shotsMadeX, shotsMadeY, shotsMissedX, shotsMissedY]
        
    
        
        
    def average(self, dataList):
        
        return sum(dataList)/len(dataList)
        
    def unitDeviation(self, dataList):
        deviationList = []
        ave = self.average(dataList)
        
        for data in range(len(dataList)):
            diff = abs(dataList[data] - ave)
            deviationList.append(diff)
            
        return deviationList
        
        
        
   
        


def getStats(PlayerID = 201939):
    url = 'http://stats.nba.com/stats/playergamelog?LeagueID=00&PlayerID='+ str(PlayerID) +'&Season=2015-16&SeasonType=Regular+Season'
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    return data
    
def getShotStats(PlayerID = 201939):
    url = 'http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID='+ str(PlayerID) +'&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    return data
    
def getShotLocStats(PlayerID = 201939):
    url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPARAMS=2015-16&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID='+str(PlayerID)+'&PlusMinus=N&Position=&Rank=N&RookieYear=&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&showZones=0'
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    return data


p = player(getStats(), getShotStats(), getShotLocStats())

#print p.shotLocations()
locations = p.shotLocations()
pylab.figure('shotchart')

pylab.plot(locations[2], locations[3], 'r.')
pylab.plot(locations[0], locations[1], 'g.')

pylab.xlim(-350, 350)
pylab.ylim(-100, 500)
pylab.show('shotchart')




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

pylab.figure(3)
pylab.plot(p.threesMadeEachGame(), 'gD')
pylab.xlabel('game')
pylab.ylabel('Threes')
pylab.xlim(-1, len(p.threesMadeEachGame())+1)
pylab.ylim(-1, 15)
pylab.show()

print p.threesMadeEachGame()
