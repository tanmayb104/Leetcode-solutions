class UndergroundSystem:

    def __init__(self):
        self.p={}
        self.g={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.p[id]=[t,stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        a,b=self.p[id]
        time=t-a
        if(b in self.g and stationName in self.g[b]):
            self.g[b][stationName].append(time)
        elif(b in self.g):
            self.g[b][stationName]=[time]
        else:
            self.g[b]={}
            self.g[b][stationName]=[time]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print(self.g,startStation,endStation)
        return sum(self.g[startStation][endStation])/len(self.g[startStation][endStation])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)