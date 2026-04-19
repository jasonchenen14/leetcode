import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0))
            
        events.sort()
        
        max_heap = [(0, float('inf'))]
        res = [[0, 0]]
        
        for x, neg_H, R in events:
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
                
            if neg_H != 0:
                heapq.heappush(max_heap, (neg_H, R))
                
            curr_max_H = -max_heap[0][0]
            if res[-1][1] != curr_max_H:
                res.append([x, curr_max_H])
                
        return res[1:]
