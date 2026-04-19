import random
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.valid_len = n - len(blacklist)
        self.mapping = {}
        b_set = set(blacklist)
        
        last = n - 1
        for b in blacklist:
            if b < self.valid_len:
                while last in b_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        idx = random.randint(0, self.valid_len - 1)
        return self.mapping.get(idx, idx)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
