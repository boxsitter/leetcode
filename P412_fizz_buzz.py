# ID: 412 | Fizz Buzz
# URL: https://leetcode.com/problems/fizz-buzz/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(n):
            to_append = ""
            if (i + 1) % 3 == 0:
                to_append = "Fizz"
            if (i + 1) % 5 == 0:
                to_append += "Buzz"
            if to_append == "":
                to_append = str(i + 1)
            output.append(to_append)
        return output

        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    print(sol.fizzBuzz(5))
    print("--- Local Run Complete ---")