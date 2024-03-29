def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
        
    return bucket

def bucket_sort(arr, n):

    _min = min(arr)
    _max = max(arr)
    buckets = [[] for _ in range(n)]
    
    for num in arr:
        
        index = int((num - _min)/((_max - _min)/(n-1)))
        print(index)
        buckets[index].append(num)
    
    print(buckets)
    for bucket in buckets:
        insertion_sort(bucket)
    
    ind = 0
    for bucket in buckets:
        for num in bucket:
            arr[ind] = num
            ind += 1
        
    return arr

# Test cases
def test():
    # Test case 1
    
    arr = [0.897, 0.897, 0.656, 0.1234, 0.665, 0.3434]
    print(bucket_sort(arr, len(arr)))
    
    # # Test case 2
    # arr = [0.5, 0.1, 0.9, 0.3, 0.7]
    # assert bucket_sort(arr, len(arr)) == [0.1, 0.3, 0.5, 0.7, 0.9], "Test case 2 failed"
    
    #  # Test case 3
    # arr = [3.9, 0.9, 1.9, 5.9, 2.9, 4.9]
    # assert bucket_sort(arr, len(arr)) == [0.9, 1.9, 2.9, 3.9, 4.9, 5.9], "Test case 3 failed"
    
    # print("All test cases passed!")

# Run test cases
test()
