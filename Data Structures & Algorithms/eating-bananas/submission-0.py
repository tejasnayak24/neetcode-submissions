from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            k=(l+r)//2
            hours=0
            for pile in piles:
                hours+=ceil(pile/k)
            if hours<=h:
                answer=k
                r=k-1
            else:
                l=k+1
        return answer
                
        