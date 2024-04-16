# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap()
        heap.heapify(nums)
        while k > 1:
            heap.delete()
            k -= 1
        return heap.delete()
