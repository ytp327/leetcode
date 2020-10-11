<h1> 316. Remove Duplicate Letters --Medium</h1> 
<p>Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is <b>the smallest in lexicographical order</b> among all possible results.</p>

<pre>
<b>Example 1:</b>
Input: s = "bcabc"
Output: "abc"
<b>Example 2:</b>
Input: s = "cbacdcbc"
Output: "acdb"
</pre>


``` python
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, seen = [], set()
        last_occurrence = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
```