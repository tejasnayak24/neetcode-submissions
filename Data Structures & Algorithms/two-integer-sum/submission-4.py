class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return[seen[diff],index]
            else:
                seen[num]=index        