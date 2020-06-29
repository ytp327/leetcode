def mergeSort(nums):
    mid = len(nums) // 2
    if mid:
        l, r = mergeSort(nums[:mid]), mergeSort(nums[mid:])
        for i in range(len(nums)-1, -1, -1):
            if not r or l and l[-1] > r[-1]:
                nums[i] = l.pop()
            else:
                nums[i] = r.pop()
    return nums

print(mergeSort([3,2,1,6,-1,21,0]))