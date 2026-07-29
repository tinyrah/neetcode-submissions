class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # buckets = [[] for _ in range(len(nums)+1)]

        # for num, freq in count.items():
        #     buckets[freq].append(num)
        # res = []
        # for i in range(len(nums)-1,-1,-1):
        #     for num in buckets[i]:
        #         res.append(num)
        #         if len(res) == 1:
        #             return res[0]j

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        print(count)
        
        most_freq_number = nums[0]
        most_freq_number_count = count[most_freq_number]

        for num, freq in count.items():
            print(num)
            print(freq)
            print("most frequent number: " + str(most_freq_number))
            print("most frequent number count: " + str(most_freq_number_count))
            if freq > most_freq_number_count:
                most_freq_number = num
                print("most frequent number updated to " + str(most_freq_number))
                most_freq_number_count
            print("most frequent number: " + str(most_freq_number))
            print("most frequent number count: " + str(most_freq_number_count))

        return most_freq_number
