class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @functools.lru_cache(None)
        def _search(rest_k: int, pile_pos: int) -> int:
            if rest_k == 0 or pile_pos == len(piles): return 0
            current_mv_found = _search(rest_k, pile_pos+1)
            current_pile = piles[pile_pos]
            accum_coin_value = 0
            for i in range(min(rest_k, len(current_pile))):
                accum_coin_value += current_pile[i]
                current_mv_found = max(
                    current_mv_found, 
                    accum_coin_value + _search(rest_k-i-1, pile_pos+1))
            return current_mv_found
        return _search(k, 0)