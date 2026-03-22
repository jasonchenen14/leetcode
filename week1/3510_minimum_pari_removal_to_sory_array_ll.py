import heapq

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.id = idx
        self.prev = None
        self.next = None
        self.deleted = False

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        nodes = [Node(x, i) for i, x in enumerate(nums)]
        inv_count = 0
        
        for i in range(n - 1):
            nodes[i].next = nodes[i+1]
            nodes[i+1].prev = nodes[i]
            if nums[i] > nums[i+1]:
                inv_count += 1
                
        if inv_count == 0:
            return 0
            
        pq = []
        counter = 0
        for i in range(n - 1):
            heapq.heappush(pq, (nodes[i].val + nodes[i+1].val, nodes[i].id, counter, nodes[i], nodes[i+1]))
            counter += 1
            
        ops = 0
        while pq:
            s, node_id, _, left, right = heapq.heappop(pq)
            
            if left.deleted or right.deleted:
                continue
                
            ops += 1
            
            if left.prev and left.prev.val > left.val:
                inv_count -= 1
            if left.val > right.val:
                inv_count -= 1
            if right.next and right.val > right.next.val:
                inv_count -= 1
                    
            new_node = Node(left.val + right.val, left.id)
            new_node.prev = left.prev
            new_node.next = right.next
            
            if new_node.prev:
                new_node.prev.next = new_node
                if new_node.prev.val > new_node.val:
                    inv_count += 1
            if new_node.next:
                new_node.next.prev = new_node
                if new_node.val > new_node.next.val:
                    inv_count += 1
                    
            left.deleted = True
            right.deleted = True
            
            if inv_count == 0:
                return ops
                
            if new_node.prev:
                heapq.heappush(pq, (new_node.prev.val + new_node.val, new_node.prev.id, counter, new_node.prev, new_node))
                counter += 1
            if new_node.next:
                heapq.heappush(pq, (new_node.val + new_node.next.val, new_node.id, counter, new_node, new_node.next))
                counter += 1
                
        return ops
