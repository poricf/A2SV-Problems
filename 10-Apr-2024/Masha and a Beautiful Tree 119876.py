# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
    flag = True
    for j in range(len(left)):
        if left[j] < right[0]:
            flag = False


    if flag:
        ans[0] += 1
        merged.extend(right)
        merged.extend(left)
    else:
        merged.extend(left)
        merged.extend(right)
        
    

    return merged

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = [0]
    m = mergeSort(a,ans)
    
    print(ans[0] if m == sorted(a) else -1)

# t = 1
t = int(input())

for i in range(t):
    solve()