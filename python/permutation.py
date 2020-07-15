def nextPermutation(nums):
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1  # nums[i:] in decreasing order
    if i > 0:
        j = i + 1
        while j < len(nums) and nums[j] > nums[i - 1]:
            j += 1  # nums[i-1] and nums[j-1] are closest
        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
    nums[i:] = nums[i:][::-1]
    return nums

def previousPermutation(nums):
    i = len(nums) - 1
    while i > 0 and nums[i] >= nums[i - 1]:
        i -= 1  # nums[i:] in ascending order
    if i > 0:
        j = i + 1
        while j < len(nums) and nums[j] < nums[i - 1]:
            j += 1  # nums[i-1] and nums[j-1] are closest
        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
    nums[i:] = nums[i:][::-1]
    return nums

nums = [1,2,3,3]
for i in range(6):
    print(nums)
    nums = previousPermutation(nums)