<h1> 72. Edit Distance --Hard</h1> 
<p>Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:
<br>
1. Insert a character<br>
2. Delete a character<br>
3. Replace a character</p>

<pre>
<b>Example 1:</b>
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
<b>Example 2:</b>
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
</pre>


``` python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n=len(word1), len(word2)
        cur=[j for j in range(n+1)]
        for i in range(1,m+1):
            pre, cur=cur, [i]
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    cur.append(pre[j-1])
                else:
                    cur.append(1+min(pre[j-1], cur[j-1], pre[j]))
        return cur[-1]
```