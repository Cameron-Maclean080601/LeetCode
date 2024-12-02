class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        function to start in the middle of the word and mvoe out left and right
        ensure that the charcters match
        if they dont then not longest paladrome
        """
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.moveFromMiddleOut(s, i, i)
            len2 = self.moveFromMiddleOut(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]

    def moveFromMiddleOut(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

X = Solution()
X.longestPalindrome("babad")