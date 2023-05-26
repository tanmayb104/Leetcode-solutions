class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        self.dp = {}

        def recursiveStoneGame(start, M):            
            if start >= N:
                return 0
            if N - start <= 2*M:
                return sum(piles[start:])
            
            if (start, M) in self.dp:
                return self.dp[(start, M)]

            my_score = 0
            total_score = sum(piles[start:])
            for x in range(1, 2*M+1):
                opponent_score = recursiveStoneGame(start+x, max(x, M))
                my_score = max(my_score, total_score - opponent_score)
                
            self.dp[(start, M)] = my_score
                
            return my_score
        
        
        return recursiveStoneGame(0, 1)