def binarySearch(nums,target):
    l, r=0, len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1

def binarySearch2(nums, target):
    left, right=0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
a=[1,1,1,2,2,2,4,5]
i=binarySearch2(a,2)
a.insert(i,2)
print(i)