# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(nums, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and nums[l] > nums[largest]:
        largest = l
    if r < n and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

def insert(nums, i): # insert i into maxheap
    nums.append(i)
    n=len(nums)-1
    parent=(n-1)//2
    while parent>=0 and nums[n]>nums[parent]:
        nums[n], nums[parent]=nums[parent], nums[n]
        parent, n=(parent-1)//2, parent

def delete(nums): # can only delete element at index 0
    nums[0], nums[len(nums)-1]=nums[len(nums)-1], nums[0]
    nums.pop()
    heapify(nums, len(nums)-1, 0)

def heapsort(nums):
    n=len(nums)
    for i in range(n//2, -1, -1):
        heapify(nums, n, i)
    for i in range(n-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

a=[1,2,3,4,1,2,0]
heapsort(a)
print(a)