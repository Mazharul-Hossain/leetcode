from typing import List

global ans, transfer_counter, count


class Solution:
    # https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/discuss/866387/Java-Backtracking-Straightforward-No-Masking
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        global ans, transfer_counter, count
        ans, count = 0, 0
        transfer_counter = [0 for _ in range(n)]

        # @lru_cache(None)
        def helper(index: int, num: int):
            global ans, transfer_counter, count
            count += 1

            print("#{} transaction#{}: local ans: {}".format(count, index, num))
            # Traverse all n buildings to see if they are all 0. (means balanced)
            if index == len(requests):
                for i in transfer_counter:
                    if i != 0:
                        return
                ans = max(ans, num)
                return

            # Not Choose the request
            if requests[index][0] != requests[index][1]:
                helper(index + 1, num)

            # Choose this request
            transfer_counter[requests[index][0]] += 1
            transfer_counter[requests[index][1]] -= 1
            helper(index + 1, num + 1)

            transfer_counter[requests[index][0]] -= 1
            transfer_counter[requests[index][1]] += 1

        helper(0, 0)
        return ans


obj = Solution()
print(5, obj.maximumRequests(n=5, requests=[[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))
print(3, obj.maximumRequests(n=3, requests=[[0, 0], [1, 2], [2, 1]]))
print(4, obj.maximumRequests(n=4, requests=[[0, 3], [3, 1], [1, 2], [2, 0]]))
