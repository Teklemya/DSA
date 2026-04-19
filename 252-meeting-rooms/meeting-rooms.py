class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ''' 
        U - Given an array of meeting intervals, where each interval is [start, end], 
            determine if a person 
            can attend all meetings (i.e., no meetings overlap).

            Input: List of intervals, e.g., [[0,30],[5,10],[15,20]]
            Output: True if no meetings overlap, False otherwise
            Example:
            [[0,30],[5,10],[15,20]] → False (overlap)
            [[7,10],[2,4]] → True (no overlap)
            Constraints: 0 <= start < end

        M - Common technique: Sort intervals by start time, 
            then check for overlaps between consecutive intervals.
        P - Sort the intervals by their start time.
            Iterate through the sorted intervals.
            For each interval, compare its end time to the start time of the next interval.
            If the next meeting starts before the current one ends, return False (overlap found).
            If no overlaps are found after checking all intervals, return True.

        '''

        intervals.sort(key=lambda x: x[0])
        print(intervals)
        endTime = 0

        for i in range(len(intervals) - 1):
            endTime = intervals[i][1]
            #if the next elem start tiem is less than this end tiem then False
            if intervals[i + 1][0] < endTime:
                return False
        return True






























        # intervals.sort(key = lambda x: x[0])
        # endTime = 0
        # for i in range(len(intervals) - 1):
        #     endTime = intervals[i][1]
        #     if intervals[i + 1][0] < endTime:
        #         return False
        # return True