# Problem: My Calendar II - https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:


    def __init__(self):
        self.single = []
        self.double = []

    def book(self, start: int, end: int) -> bool:
        for startd, endd in self.double:
            if max(start, startd) < min(end, endd):  # nvlap
                return False
        
        for sng_start, sng_end in self.single:
            overlap_start = max(start, sng_start)
            overlap_end = min(end, sng_end)
            if overlap_start < overlap_end: #volap
                self.double.append((overlap_start, overlap_end))
        
        self.single.append((start, end))
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)