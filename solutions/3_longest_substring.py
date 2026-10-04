# Problem: Longest substring 
# Difficulty: Midium 
# Language: python 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        size=0
        for i in range(length):
            my_set=set()
            for j in range(i, length):
                if s[j] in my_set:
                    break
                my_set.add(s[j])
                size=max(size,j-i+1)
        return size