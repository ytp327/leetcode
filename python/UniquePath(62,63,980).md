<h1> 62. Unique Paths -Medium</h1> 
<p>A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).</p>
<p>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).</p>
<p>How many possible unique paths are there?</p>

``` python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [1 for i in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                res[j] += res[j-1]
        return res[-1]
```



<h1>63. Unique Paths II</h1>