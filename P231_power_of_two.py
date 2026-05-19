# ID: 231 | Power of Two
# URL: https://leetcode.com/problems/power-of-two/
from operator import truediv
from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            return n & (n - 1) == 0
        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(16))
    print("--- Local Run Complete ---")