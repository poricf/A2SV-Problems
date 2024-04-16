# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

from typing import List

class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None

        self.swap(0, len(self.heap) - 1)
        deleted_value = self.heap.pop()
        self.heapify_down(0)

        return deleted_value

    def heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)
        heap_size = len(self.heap)

        if left < heap_size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < heap_size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.heapify_down(largest)

    def heapify(self, nums):
        self.heap = nums
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = Heap()
        heap.heapify(stones)
        ans = 0
        while len(stones) > 1:
            y = heap.delete()
            x = heap.delete()
            if y - x:
                heap.insert(y - x)
        if stones: ans = stones[0]
        return ans