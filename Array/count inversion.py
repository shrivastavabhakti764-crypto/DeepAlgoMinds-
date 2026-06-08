class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        req = {}
        for end, cnt in requirements:
            if end in req and req[end] != cnt:
                return 0
            req[end] = cnt

        maxInv = max(req.values(), default=0)

        dp = [0] * (maxInv + 1)
        dp[0] = 1

        for length in range(1, n + 1):
            new = [0] * (maxInv + 1)

            prefix = [0] * (maxInv + 2)
            for i in range(maxInv + 1):
                prefix[i + 1] = (prefix[i] + dp[i]) % MOD

            for inv in range(maxInv + 1):
                left = max(0, inv - (length - 1))
                right = inv

                new[inv] = (prefix[right + 1] - prefix[left]) % MOD

            if (length - 1) in req:
                need = req[length - 1]
                temp = [0] * (maxInv + 1)
                if need <= maxInv:
                    temp[need] = new[need]
                new = temp

            dp = new

        return sum(dp) % MOD