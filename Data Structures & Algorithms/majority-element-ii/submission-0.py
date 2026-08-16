from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums)//3
        res = []
        freq= Counter(nums)
        for num in freq:
            if freq[num]>k:
                res.append(num)
        return res
        