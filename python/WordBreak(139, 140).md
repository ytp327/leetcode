<h1> 139. Word Break --Medium</h1> 
<p>Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.</p>
<p>The same word in the dictionary may be reused multiple times in the segmentation.<br>
You may assume the dictionary does not contain duplicate words.</p>

<pre>
<b>Example1:</b>
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
<b>Example2:</b>
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
<b>Example3:</b>
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
</pre>

``` python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            for word in wordDict:
                if word == s[i-len(word):i] and dp[i-len(word)]:
                    dp[i] = 1
                    break
        return dp[-1]
```



<h1>140. Word Break II --Hard</h1>
<p>Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.</p>
<p>The same word in the dictionary may be reused multiple times in the segmentation.<br>
You may assume the dictionary does not contain duplicate words.</p>

<pre>
<b>Example1:</b>
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
<b>Example2:</b>
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
<b>Example3:</b>
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
</pre>

``` python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if set(s) > set("".join(wordDict)):
            return []
        dp = [[] for _ in range(len(s)+1)]
        dp[0] = [[]]
        for i in range(1, len(s)+1):
            for word in wordDict:
                if s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] += [x+[word] for x in dp[i-len(word)]]
        return [" ".join(x) for x in dp[-1]]
```