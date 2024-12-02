class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = []
        s_list = []
        if len(s) != len(t):
            return False
        
        for i in range (len(t)):
            t_list.append(t[i])
            s_list.append(s[i])
        t_list.sort()
        s_list.sort()
        if s_list == t_list:
            return True
        else:
            return False
        
Y = Solution()
Y.isAnagram("carraces", "racecar")