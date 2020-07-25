<h1> 269. Alien Dictionary --Hard</h1> 
<p>There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where <b>words are sorted lexicographically by the rules of this new language</b>. Derive the order of letters in this language.</p>
<p>Note:
You may assume all letters are in lowercase.<br>
If the order is invalid, return an empty string.<br>
There may be multiple valid order of letters, return any one of them is fine.</p>

<pre>
<b>Example1:</b>
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

<b>Example2:</b>
Input:
[
  "z",
  "x"
]

Output: "zx"

<b>Example3:</b>
Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
</pre>

solution1 --topological sort:
``` python
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = {x:set() for x in set("".join(words))}
        visit = {x:-1 for x in set("".join(words))}
        for i in range(len(words)-1):
            minLen = min(len(words[i]), len(words[i+1]))
            for j in range(minLen):
                if words[i][j] != words[i+1][j]:
                    if words[i+1][j] not in graph[words[i][j]]:
                        graph[words[i][j]].add(words[i+1][j])
                    break
                elif j == minLen - 1 and len(words[i]) > len(words[i+1]):
                    return ""
        self.res = ""
        def dfs(char):
            if visit[char] == -1:
                visit[char] += 1
                for nextChar in graph[char]:
                    if not dfs(nextChar): return False
                visit[char] += 1
                self.res = char + self.res
            elif visit[char] == 0: return False
            return True
        for x in graph.keys():
            if not dfs(x): return ""
        return self.res
```

solution2 --graph traversal in indegree increasing order:
``` python
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = {x:set() for x in set("".join(words))}
        indegree = collections.defaultdict(int)
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    if words[i+1][j] not in graph[words[i][j]]:
                        graph[words[i][j]].add(words[i+1][j])
                        indegree[words[i+1][j]] += 1
                    break
                elif j == min(len(words[i]), len(words[i+1])) - 1 and len(words[i]) > len(words[i+1]):
                    return ""
        res, queue = "", collections.deque([char for char in graph if indegree[char] == 0]) 
        while queue:
            curChar = queue.popleft()
            res += curChar
            for nextChar in graph[curChar]:
                indegree[nextChar] -= 1
                if indegree[nextChar] == 0:
                    queue.append(nextChar)
        return res if len(res) == len(graph) else ""
```