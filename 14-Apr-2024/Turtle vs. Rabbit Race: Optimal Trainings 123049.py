# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

from sys import stdin, stdout
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from math import *



def input():
    return stdin.readline().strip()

def print(*obj, sep = ' ', end = '\n'):
    objs = [str(i) for i in obj]
    return stdout.write(str(sep.join(objs)) + end)
    
def int_space():
    return list(map(int,input().split()))

def int_string():
    return [int(i) for i in input()]

def calc(m, u, l):
    s = prefix[m + 1] - prefix[l - 1]
    return (s * (2 * u - s + 1)) / 2



for i in range(int(input())):
    n = int(input())
    nums = int_space()

    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    answers = []

    for j in range(int(input())):

        l, u = int_space()

        left = l - 1
        right = n - 1

        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            s = prefix[mid + 1] - prefix[l - 1]
            
            if s >= u:
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1

        if ans > l - 1 and calc(ans - 1, u, l) >= calc(ans, u, l):
            ans -= 1

        answers.append(ans + 1)

    print(*answers)
    
