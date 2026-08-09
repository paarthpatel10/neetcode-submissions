class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res =[]
        for ch in nums:
            if ch in freq:
                freq[ch] +=1
            else:
                freq[ch] =1
        for i in range(k):
            max_num = None
            max_freq =0
            for num in freq:
                if freq[num]>max_freq:
                    max_freq = freq[num]
                    max_num =num
            res.append(max_num)
            del freq[max_num]



        return res

                

        