import heapq
def topKFrequent(nums, k):
        freq={}
        sort_list=[]
        for n in nums:
          freq[n]=freq.get(n,0)+1
        heap=[]
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap)>k:
                 heapq.heappop(heap)
        return [num for count,num in heap]
nums=[1,2,3,2,3,1,1,2,1]
k=2
print(topKFrequent(nums,k))