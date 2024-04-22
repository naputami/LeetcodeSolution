class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = {};
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i][::-1] == words[j]:
                    if words[i] not in count:
                        count[words[i]] = 1
                        
        return len(count)
        
        