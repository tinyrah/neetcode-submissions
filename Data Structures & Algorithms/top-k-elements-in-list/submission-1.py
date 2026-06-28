class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for n in nums:
            if n not in num_freq:
                num_freq[n] = 0
            num_freq[n] += 1
        
        count_arr = [[] for _ in range(len(nums)+1)]

        for num, count in num_freq.items():
            count_arr[count].append(num)
        
        ans = []

        for i in range(len(count_arr)-1,-1,-1):
            for n in count_arr[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans