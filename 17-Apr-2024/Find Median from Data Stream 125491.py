# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1

        if self.count % 2 != 0:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            val1 = heappop(self.min_heap)
            val2 = heappop(self.max_heap)

            heappush(self.min_heap,-val2)
            heappush(self.max_heap,-val1)




    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()