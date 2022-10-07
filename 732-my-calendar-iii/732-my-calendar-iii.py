from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.lines = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.lines[start] = self.lines.get(start, 0) + 1
        self.lines[end] = self.lines.get(end, 0) - 1
        return max(accumulate(self.lines.values()))
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)