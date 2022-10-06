class TimeMap:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)