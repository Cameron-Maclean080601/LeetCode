# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s = s.strip()
#         positive = True
#         started = False
#         str_s = []
#         start = 0
#         s_int = 0
#         end = len(s)
#         i = 0
#         one_free = False
#         nums = ["1","2","3","4","5","6","7","8","9"]
#         for char in s: 
#             i += 1
#             if char == "-" and one_free == False:
#                 positive = False 
#                 one_free = True
#             elif char == "+" and one_free == False:
#                 positive = True
#                 one_free = True
#             elif char in nums and started == False:
#                 start = s.index(char)
#                 started = True
#             elif char not in nums and char != "0":
#                 end = s.index(char)
#                 break
#             elif char == "0" and started == False:
#                 index_test = s.index(char)
#                 if s[index_test + 1] not in nums:
#                     started = True
#                     end_char = s[index_test + 1]
#                     end = s.index(end_char)
#                     start = s.index(char)
#                     break
#             elif i == len(s):
#                 end = len(s)
#             elif char not in nums:
#                 end = 0
#                 start = 0
#                 started == False
#                 break


#         if started == True:
#             for i in range(start,end):
#                 str_s += str(s[i])
#             s_int = int(''.join(map(str, str_s)))

#         if positive == False:
#             s_int = - s_int

#         if s_int > (2**31-1):
#             s_int = 2147483647

#         if s_int < (-2**31):
#             s_int = -2147483648
#         return s_int
# Y = Solution()
# X = Y.myAtoi("21474836460")
# print(X)

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        i, n = 0, len(s)
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for optional sign
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Convert digits to integer
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        
        return sign * result

        
            