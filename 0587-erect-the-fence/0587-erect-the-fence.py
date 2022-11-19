class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def compare_slopes(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2) 
        upper, lower  = [], []
        for point in sorted(trees):
            while len(lower) >= 2 and compare_slopes(lower[-2], lower[-1], point) < 0: lower.pop()
            while len(upper) >= 2 and compare_slopes(upper[-2], upper[-1], point) > 0: upper.pop()
            lower.append(tuple(point))
            upper.append(tuple(point))   
        return list(set(lower + upper))