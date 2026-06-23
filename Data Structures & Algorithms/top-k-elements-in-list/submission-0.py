from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=Counter(nums).most_common(k)
        ans=[]
        for num,count in m:
            ans.append(num)
        return ans
        