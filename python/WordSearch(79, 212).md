<h1> 79. Word Search --Medium</h1> 
<p>Given a 2D board and a word, find if the word exists in the grid.</p>
<p>The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<pre>
<b>Example:</b>
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.</pre>

``` python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n=len(board), len(board[0])
        if m * n < len(word): return False
        def dfs(i, j, startIndex):
            if startIndex == len(word):
                return True
            if i<0 or j<0 or i>=m or j>=n:
                return False
            if board[i][j] != word[startIndex]:
                return False
            temp, board[i][j] = board[i][j], '#'
            res = dfs(i-1, j, startIndex+1) or dfs(i+1 ,j, startIndex+1)\
            or dfs(i ,j-1, startIndex+1) or dfs(i ,j+1, startIndex+1)
            board[i][j] = temp
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False
```



<h1>212. Word Search II --Hard</h1>
<p>Given a 2D board and a list of words from the dictionary, find all words in the board.</p>
<p>Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.</p>

<pre>
<b>Example:</b>
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]</pre>

```python
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie, m, n = {}, len(board), len(board[0])
        for word in words:
            if len(word) > m * n: continue
            t = trie
            for w in word:
                if w not in t:
                    t[w] = {}
                t = t[w]
            t['#'] = '#'
        res = set()
        def dfs(i, j, trie, path):
            if '#' in trie:
                res.add(path)
            if i<0 or j<0 or i == m or j == n or board[i][j] not in trie:
                return
            temp, board[i][j] = board[i][j], '@'
            dfs(i-1, j, trie[temp], path+temp)
            dfs(i+1, j, trie[temp], path+temp)
            dfs(i, j-1, trie[temp], path+temp)
            dfs(i, j+1, trie[temp], path+temp)
            board[i][j] = temp
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, '')
        return res
```