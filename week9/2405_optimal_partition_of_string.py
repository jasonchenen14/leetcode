class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        seen = set()
        
        for char in s:
            if char in seen:
                count += 1
                seen.clear()
            seen.add(char)
            
        return count
