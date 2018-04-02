class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num = int(len(strs))
        result = ""
        if num <= 0:
            return result
        else:
            One = int(len(strs[0]))
            for k in range(num - 1):
                Min = min(One, len(strs[k]))
            for i in range(num - 1):
                j = 0
                while j < Min:
                    if strs[0][j] != strs[i][j]:
                        break
                    j += 1

                if j == 0:
                    return result
                result += strs[0][:j]
            return result


if __name__ == "__main__":
    print Solution().longestCommonPrefix("")
