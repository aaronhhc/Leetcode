#my solution
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def isPrime(n: int) -> bool:
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False

            for d in range(3, int(n ** 0.5) + 1, 2):
                if n % d == 0:
                    return False

            return True
            
        res = 0
        reverse = int(str(n)[::-1])
        for i in range(min(n, reverse), max(n, reverse) + 1):
            if isPrime(i):
                res += i
        return res

#sieve of eratosthenes
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        reverse = int(str(n)[::-1])

        left = min(n, reverse)
        right = max(n, reverse)

        is_prime = [True] * (right + 1)

        if right >= 0:
            is_prime[0] = False
        if right >= 1:
            is_prime[1] = False

        for p in range(2, int(right ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, right + 1, p):
                    is_prime[multiple] = False

        res = 0
        for x in range(left, right + 1):
            if is_prime[x]:
                res += x

        return res