class Solution:
    def Fibonacci(self, n):
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]


s = Solution()
result = s.Fibonacci(25)
print(result)
