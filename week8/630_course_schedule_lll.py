import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        max_heap = []
        current_time = 0
        
        for duration, last_day in courses:
            current_time += duration
            heapq.heappush(max_heap, -duration)
            
            if current_time > last_day:
                current_time -= -heapq.heappop(max_heap)
                
        return len(max_heap)
