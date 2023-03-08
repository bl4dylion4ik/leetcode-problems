class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])

        res = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(prev_end, end)

        return res




####################################

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        # keep the interval that has the shorter end since longer end will overlap with other intervals
        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] < intervals[i][1]:
                count += 1
                intervals[i + 1][1] = min(intervals[i + 1][1], intervals[i][1])

        return count