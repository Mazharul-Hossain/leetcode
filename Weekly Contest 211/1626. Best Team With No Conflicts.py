from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        score_age = sorted([[age, score] for age, score in zip(ages, scores)])
        print(score_age)

        dp, length = [], len(scores)
        for i in range(length):
            dp.append(score_age[i][1])
            for j in range(i):
                if score_age[i][1] >= score_age[j][1]:
                    dp[i] = max(dp[i], score_age[i][1] + dp[j])

        return max(dp)


obj = Solution()
print(34 == obj.bestTeamScore(scores=[1, 3, 5, 10, 15], ages=[1, 2, 3, 4, 5]))
print(16 == obj.bestTeamScore(scores=[4, 5, 6, 5], ages=[2, 1, 2, 1]))
print(6 == obj.bestTeamScore(scores=[1, 2, 3, 5], ages=[8, 9, 10, 1]))
