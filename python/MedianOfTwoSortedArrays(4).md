<h1> 4. Median of Two Sorted Arrays --Hard </h1> 
<p>Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
</p>
<p>Follow up: The overall run time complexity should be O(log (m+n))</p>

<pre>
<b>Example 1:</b>
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
<b>Example 2:</b>
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
<b>Example 3:</b>
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
<b>Example 4:</b>
Input: nums1 = [], nums2 = [1]
Output: 1.00000
</pre>


``` python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # i+j=(m+n+1)//2
        m, n=len(nums1), len(nums2)
        if m>n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i
            if i > 0 and nums1[i-1] > nums2[j]:
                r = i - 1
            elif i < m and nums1[i] < nums2[j-1]:
                l = i + 1
            else:
                if i == 0:
                    maxOfLeft = nums2[j-1]
                elif j == 0:
                    maxOfLeft = nums1[i-1]
                else:
                    maxOfLeft = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2: return float(maxOfLeft)
                if i == m:
                    minOfRight = nums2[j]
                elif j == n:
                    minOfRight = nums1[i]
                else:
                    minOfRight = min(nums1[i], nums2[j])
                return (maxOfLeft + minOfRight) / 2.0
```
