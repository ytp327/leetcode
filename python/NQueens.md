<h1> 51. N-Queens --Hard</h1> 
<p>The <i>n</i>-queens puzzle is the problem of placing <i>n</i> queens on an <i>n×n</i> chessboard such that no two queens attack each other.</p>
<img src = "../pic/8-queens.png" >
<p>Given an integer <i>n</i>, return all distinct solutions to the <i>n</i>-queens puzzle.</p>
<p>Each solution contains a distinct board configuration of the <i>n</i>-queens' placement, where <code>'Q'</code> and <code>'.'</code> both indicate a queen and an empty space respectively.</p>

<pre>
<b>Example:</b>
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.</pre>

``` python
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        def dfs(col, rcSum, rcDif):
            nrow = len(col)
            if nrow == n:
                res.append(col)
                return
            for ncol in range(n):
                if ncol not in col and nrow+ncol not in rcSum and nrow-ncol not in rcDif:
                    dfs(col+[ncol], rcSum + [nrow+ncol], rcDif + [nrow-ncol])
        
        dfs([], [], [])
        return [['.' * x + 'Q' + '.' * (n-x-1) for x in sol] for sol in res]
```

<h1>52. N-Queens II --Hard</h1>
<p>The <i>n</i>-queens puzzle is the problem of placing <i>n</i> queens on an <i>n×n</i> chessboard such that no two queens attack each other.</p>
<p>Given an integer <i>n</i>, return the number of distinct solutions to the <i>n</i>-queens puzzle.</p>

<pre>
<b>Example:</b>
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]</pre>

```python
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        def dfs(col, rcSum, rcDif):
            nrow = len(col)
            if nrow == n:
                self.res += 1
                return
            for ncol in range(n):
                if ncol not in col and nrow+ncol not in rcSum and nrow-ncol not in rcDif:
                    dfs(col + [ncol], rcSum + [nrow+ncol], rcDif + [nrow-ncol])
        dfs([], [], [])
        return self.res
```