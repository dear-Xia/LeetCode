class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        answer = 0
        y = x
        if x < 0:
            return False
        else:
            while x != 0:
                answer = answer * 10 + x % 10
                x = x // 10

            if y == answer:
                return True
            else:
                return False
if __name__ == "__main__":
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(12320)
    print Solution().isPalindrome(-12321)