class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_char = dict()
        
        for i in range(len(s)):
            if s[i] not in map_char:
                map_char[s[i]] = t[i]
            else:
                if map_char[s[i]] != t[i]:
                    return False
        
        return len(map_char) == len(set(map_char.values()))