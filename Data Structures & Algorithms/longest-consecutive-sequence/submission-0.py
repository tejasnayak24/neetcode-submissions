class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numset=set(nums)
        for num in numset:
            if num-1 not in numset:
                length=0
                while num+length in numset:
                    length+=1
                longest=max(longest,length)
        return longest


        