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

<p>A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).</p>
<p>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).</p>
<p>Now consider if some obstacles are added to the grids. How many unique paths would there be?</p>

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        res=[[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            if obstacleGrid[0][j]==1:
                while j<n:
                    res[0][j]=0
                    j+=1
                break
            else:
                res[0][j]=1
        for i in range(m):
            if obstacleGrid[i][0]==1:
                while i<m:
                    res[i][0]=0
                    i+=1
                break
            else:
                res[i][0]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    res[i][j]=0
                else:
                    res[i][j]=res[i-1][j]+res[i][j-1]
        return res[m-1][n-1]
```