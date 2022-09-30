class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        x_height_right_tuples = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, "doesn't matter") for _, R, _ in buildings])   
        result, max_heap = [[0, 0]], [(0, float('inf'))]
        for x, negative_height, R in x_height_right_tuples:
            while x >= max_heap[0][1]:
                heapq.heappop(max_heap)
            if negative_height:
                heapq.heappush(max_heap, (negative_height, R))
            curr_max_height = -max_heap[0][0]
            if result[-1][1] != curr_max_height:
                result.append([x, curr_max_height])
        return result[1:] 