"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        prevend=-1
        for interview in intervals:
            if interview.start<prevend:
                return False
            
            prevend=interview.end
        return True
