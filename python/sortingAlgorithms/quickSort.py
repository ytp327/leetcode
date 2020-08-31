import random
def partition(nums, start, end):
    j = start
    for i in range(start, end):
        if nums[i] < nums[end]:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    nums[j], nums[end] = nums[end], nums[j]
    return j


def _quicksort(nums, start, end):
    if start >= end: return
    p = partition(nums, start, end)
    _quicksort(nums, start, p - 1)
    _quicksort(nums, p + 1, end)


def quicksort(nums):
    random.shuffle(nums)
    _quicksort(nums, 0, len(nums) - 1)

a=[5,4,3,2,1,23,4,2,20,0,0,2,1]
quicksort(a)
print(a)