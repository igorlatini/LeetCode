class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        n_operations = 0
        while(True):
            try:
                min_1 = heapq.heappop(nums)
                if min_1 >= k:
                    return n_operations
                min_2 = heapq.heappop(nums)
                n_operations += 1
                value = min(min_1, min_2) * 2 + max(min_1, min_2)
                heapq.heappush(nums, value)
            except Exception as ex:
                return n_operations

#General idea: use heap to make it faster
