class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        if s[0] == '0':
            return 0
            
        prev2 = 1
        prev1 = 9 if s[0] == '*' else 1
        
        for i in range(1, len(s)):
            current = 0
            
            if s[i] == '*':
                current = (current + 9 * prev1) % MOD
            elif s[i] != '0':
                current = (current + prev1) % MOD
                
            if s[i-1] == '*':
                if s[i] == '*':
                    current = (current + 15 * prev2) % MOD
                elif s[i] <= '6':
                    current = (current + 2 * prev2) % MOD
                else:
                    current = (current + prev2) % MOD
            elif s[i-1] == '1':
                if s[i] == '*':
                    current = (current + 9 * prev2) % MOD
                else:
                    current = (current + prev2) % MOD
            elif s[i-1] == '2':
                if s[i] == '*':
                    current = (current + 6 * prev2) % MOD
                elif s[i] <= '6':
                    current = (current + prev2) % MOD
                    
            prev2 = prev1
            prev1 = current
            
        return prev1
