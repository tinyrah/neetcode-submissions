class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        print(count)
        bucket = [[] for _ in range(len(nums)+1)]
        print(bucket)

        for num, freq in count.items():
            bucket[freq].append(num)
        print(bucket)
        
        ans = []

        for i in range(len(bucket)-1,-1,-1):
            for number in bucket[i]:
                ans.append(number)
                if len(ans) == k:
                    return ans
        