from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=Counter(nums).most_common(k)
        ans=[]
        for num,count in nums:
            ans.append(num)
        return ans
        
        