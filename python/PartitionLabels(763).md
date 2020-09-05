<h1> 763. Partition Labels --Medium </h1> 
<p>A string <code>S</code> of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.</p>

<pre>
<b>Example1:</b>
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
</pre>

solution1 --topological sort:
``` python
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {x: i for i, x in enumerate(S)}
        start, j = 0, 0
        res = []
        for i, x in enumerate(S):
            j = max(j, last[x])
            if i == j:
                res.append(j - start + 1)
                start = j + 1
        return res
```