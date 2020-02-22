class Solution:
    def maxEvents(self, events: [[int]]) -> int:
        import heapq
        heapq.heapify(events)
        ans = 0
        day = 1
        while events:
            start, end = heapq.heappop(events)
            print("[{}, {}]".format(start, end))
            if start>=day:
                ans += 1
                day = start + 1
            elif day<=end:
                heapq.heappush(events, [day,end])
        return ans
            



events = [[1,4],[4,4],[2,2],[3,4],[1,1]]

print(Solution().maxEvents(events))