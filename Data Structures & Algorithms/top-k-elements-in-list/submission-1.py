from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):

        # Step 1: Count frequencies
        freq = Counter(nums)

        # Step 2: Create heap
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        # Step 3: Store result
        result = []

        # Step 4: Extract top k
        for i in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)

        return result