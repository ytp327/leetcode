<h1> 378. Kth Smallest Element in a Sorted Matrix --Medium</h1> 
<p>Given a <i>n</i> x <i>n</i> matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.</p>
<p>Note that it is the kth smallest element in the sorted order, not the kth distinct element. You may assume k is always valid, 1 ≤ k ≤ n^2.</p>

<pre>
<b>Example 1:</b>
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
</pre>


``` python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def count(target): 
            # how many numbers are <= target, O(len(matrix))
            i, j, res = 0, len(matrix)-1, 0
            while i < len(matrix) and j >= 0:
                if matrix[i][j] <= target: # not < !!
                    res += j+1
                    i += 1 # going down
                else:
                    j -= 1 # going left
            return res
        
        l, r = matrix[0][0], matrix[-1][-1]
        while l <= r: # binary search, O(lg(Max-Min))
            mid = (l + r) // 2
            c = count(mid)
            if c < k:
                l = mid + 1
            else:
                r = mid - 1
        return l
```