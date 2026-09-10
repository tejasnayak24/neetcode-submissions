from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        nums=Counter(nums).most_common(k)
        for num,index in nums:
            res.append(num)
        return res
        