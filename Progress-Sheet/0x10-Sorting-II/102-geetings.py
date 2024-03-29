from collections import *
from bisect import *
from itertools import *

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

    def mergeSort(nums,ans):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sorted_left = mergeSort(left,ans)
        sorted_right = mergeSort(right,ans)

        return merge(sorted_left, sorted_right,ans)

    def merge(left, right,ans):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                ind = bisect_right(left, right[j])
                if ind < len(left):
                    ans[0] += len(left) - ind
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        

        return merged

def solve():
    n = int(input())
    pairs = []
    for i in range(n):
        start , end = invr()
        pairs.append([start,end])
    pairs.sort()
    nums = []
    for pair in pairs:
        nums.append(pair[1])
    
    ans = [0]
    mergeSort(nums,ans)

    print(ans[0])


t = int(input())

for _ in range(t):
    solve()