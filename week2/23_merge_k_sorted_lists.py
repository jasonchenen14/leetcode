import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        pq = []
        
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, i, node))
                
        while pq:
            val, i, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
                
        return dummy.next
