<h1> 10. Regular Expression Matching --Hard</h1> 
<p>Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:
<br>
1.<code>'.'</code> Matches any single character.
<br>​​​​
2.<code>'*'</code> Matches zero or more of the preceding element.</p>
<p>The matching should cover the entire input string (not partial).</p>

<pre>
<b>Example 1:</b>
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
</pre>

<pre>
<b>Example 2:</b>
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
</pre>

<pre>
<b>Example 3:</b>
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
</pre>

<pre>
<b>Example 4:</b>
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
</pre>

<pre>
<b>Example 5:</b>
Input: s = "mississippi", p = "mis*is*p*."
Output: false
</pre>

``` python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pre=[1]
        for j in range(len(p)):
            if p[j]=='*':
                pre.append(pre[j-1])
            else:
                pre.append(0)
        if not s:
            return pre[-1]
        for i in range(len(s)):
            cur=[0]
            for j in range(len(p)):
                if s[i]==p[j] or p[j]=='.':
                    cur.append(pre[j])
                elif p[j]=='*':
                    if cur[j-1]:
                        cur.append(cur[j-1])
                    elif s[i]==p[j-1] or p[j-1]=='.':
                        cur.append(pre[j+1])
                    else:
                        cur.append(0)
                else:
                    cur.append(0)
            pre=cur
        return cur[-1]
```
