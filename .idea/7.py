class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        if x > 0:
            sign = 1
        else:
            sign = -1

        x = abs(x)
        while x != 0:
            answer = answer * 10 + x % 10
            x //= 10

        b = sign * answer
        if b < 2187483648 and b >= -2187483648:
            return b
        else:
            return 0
if __name__ == "__main__":
    print Solution().reverse(12321)
    print Solution().reverse(12320)
    print Solution().reverse(-12321)