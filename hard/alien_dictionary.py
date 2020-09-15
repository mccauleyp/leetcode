'''
https://leetcode.com/problems/alien-dictionary/
269. Alien Dictionary
Hard

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"

Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".

Note:

    You may assume all letters are in lowercase.
    If the order is invalid, return an empty string.
    There may be multiple valid order of letters, return any one of them is fine.
'''
class Solution:
    from collections import defaultdict, deque
    def alienOrder(self, words: List[str]) -> str:
        upstream = {char:0 for word in words for char in word}
        downstream = defaultdict(set)
        
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            length1, length2 = len(word1), len(word2)
            length = length1 if length1 < length2 else length2
            
            if length2 < length1 and word1[0:length] == word2[0:length]:
                return ""
            
            for j in range(0, length):
                letter1, letter2 = word1[j], word2[j]
                if letter1 != letter2:
                    if letter2 not in downstream[letter1]:
                        downstream[letter1].add(letter2)
                        upstream[letter2] += 1
                    break
            
        output = []
        queue = deque([char for char in upstream if upstream[char] == 0])
        while queue:
            char1 = queue.pop()
            output.append(char1)
            for char2 in downstream[char1]:
                upstream[char2] -= 1
                if upstream[char2] == 0:
                    queue.appendleft(char2)
        
        if len(upstream) > len(output):
            return ""
        
        return ''.join(output)