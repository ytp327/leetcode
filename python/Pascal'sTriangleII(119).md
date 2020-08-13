<h1>119. Pascal's Triangle II --Easy</h1> 
<p>Given a non-negative index k where k ≤ 33, return the k<sup>th</sup> index row of the Pascal's triangle.

Note that the row index starts from 0.

<br>
<img src="../pic/PascalTriangleAnimated2.gif" alt="PascalTriangle">
<br>
In Pascal's triangle, each number is the sum of the two numbers directly above it.</p>
<pre><b>Example 1:</b>

Input: 3
Output: [1,3,3,1]</pre>

``` python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, rowIndex+1):
            res.append(0)
            for j in range(i, 0, -1):
                res[j] += res[j-1]
        return res
```