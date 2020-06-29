def partition(nums, start, end):
    j=start
    for i in range(start, end):
        if nums[i]>nums[end]:
            nums[i], nums[j]=nums[j], nums[i]
            j+=1
    nums[end], nums[j]=nums[j], nums[end]
    return j

def selectKLargest(nums, start, end, k):
    p=partition(nums, start, end)
    while p!=k-1:
        if p<k:
            start, end=p+1, end
        else:
            start, end=start, p-1
        p=partition(nums, start, end)
    return nums[p] # only kth largest number
    return nums[:p+1]# top k largest number

nums=[1,2,3,5,1,2,0]
print(selectKLargest(nums, 0, len(nums)-1, 4))