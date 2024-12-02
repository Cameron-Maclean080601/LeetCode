"""
create a fucntion that changes the order of an integer, including the sign
"""

class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            x = -x
            negative = True

        reversed_array = []
        x = str(x)
        for char in range(len(x) -1 ,-1,-1):
            reversed_array.append(x[char])


        
        x_value = int(''.join(map(str, reversed_array)))

        if negative == True:
            x_value = - x_value

        x_value = int(x_value)
        if x_value > (2**31-1) or x_value < -2**31:
            x_value = 0
        return x_value





y = Solution()
print(y.reverse(120))