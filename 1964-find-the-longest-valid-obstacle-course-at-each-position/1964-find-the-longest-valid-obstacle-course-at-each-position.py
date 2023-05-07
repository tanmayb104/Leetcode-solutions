import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        result = []
        for obstacle in obstacles:
            idx = bisect.bisect_right(lis, obstacle)
            if idx == len(lis):
                lis.append(obstacle)
            else:
                lis[idx] = obstacle
            result.append(idx+1)
        return result