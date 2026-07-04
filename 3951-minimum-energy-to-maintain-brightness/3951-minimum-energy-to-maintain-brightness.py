class Solution:
    
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        def merge_intervals( intervals ):
            new_intervals = []
            intervals.sort()

            for interval in intervals:
                start, end = interval

                # if new empty or not overlapping
                if( not new_intervals or start > new_intervals[-1][1] ):
                    new_intervals.append([start, end])
                else:
                    # overlapping
                    new_intervals[-1][1] = max(new_intervals[-1][1], end)

            return new_intervals
                
        intervals = merge_intervals(intervals)
        
        active_time = 0
        for start, end in intervals:
            active_time += end - start + 1

        minimum_bulbs = (brightness + 2) // 3

        return minimum_bulbs * active_time
            
            