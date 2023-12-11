class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * (n + 1)
        p = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            j = i - 1
            while j >= 0 or p[i] != 0:
                if jobs[j][1] <= jobs[i][0]:
                    p[i + 1] = j + 1
                    break
                j -= 1

        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = max(jobs[i - 1][2] + dp[p[i]], dp[i - 1])

        return max(dp)
