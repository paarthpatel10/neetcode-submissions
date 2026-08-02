class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        if sorted(s) == sorted(t):
            return True
        
        
        return False