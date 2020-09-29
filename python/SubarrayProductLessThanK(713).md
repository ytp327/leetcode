<h1> 713. Subarray Product Less Than K --Medium</h1> 
<p>Your are given an array of positive integers nums.<br>

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.</p>

<pre>
<b>Example 1:</b>
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
</pre>


``` python
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, pro, res = 0, 1, 0
        for end in range(len(nums)):
            pro *= nums[end]
            while start <= end and pro >= k:
                pro /= nums[start]
                start += 1
            res += end - start + 1
        return res
```