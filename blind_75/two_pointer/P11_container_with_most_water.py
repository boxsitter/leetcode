# ID: 11 | Container With Most Water
# URL: https://leetcode.com/problems/container-with-most-water/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        # volume = min(height[left], height[right]) * (right - left)
        # I am going to try only moving the shorter of the two heights (left moves right, right moves left)
        # Moving the shorter of the two has the potential to find a better solution on the next turn,
        # but not vice versa
        # End condition is when two pointers are on adjacent heights

        while right > left:
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    from test_case_runner import run_tests
    run_tests(Solution(), """
Test Case 1:
-----------------------------------------------------
input:
[1,8,6,2,5,4,8,3,7]
-----------------------------------------------------
expected output:
49

Test Case 2:
-----------------------------------------------------
input:
[1,1]
-----------------------------------------------------
expected output:
1""")