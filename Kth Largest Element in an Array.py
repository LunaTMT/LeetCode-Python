import heapq

def findKthLargest(nums: list[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:    
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    
    return heap[0]



findKthLargest(nums = [3,2,1,5,6,4], k = 2)