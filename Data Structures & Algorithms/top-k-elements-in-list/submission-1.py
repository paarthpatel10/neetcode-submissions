class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res =[]
        for ch in nums:
            if ch in freq:
                freq[ch] +=1
            else:
                freq[ch] =1
       
        arr =[]
        for num,cnt in freq.items():
            arr.append([cnt,num])
        arr.sort()
        res =[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res

                

        