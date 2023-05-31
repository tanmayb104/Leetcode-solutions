class UndergroundSystem:

    def __init__(self):
        self.journey = {}
        self.history = {} # (startStation, endStation) => (allTime, allCount)

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.journey[id] = (startStation, t)
        

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        startStation, startTime = self.journey.pop(id)
        key = (startStation, endStation)
        allTime, allCount = self.history.get(key, (0, 0))
        self.history[key] = (allTime + (endTime - startTime), allCount + 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        allTime, allCount = self.history.get(key, (0, 0))
        return allTime / allCount