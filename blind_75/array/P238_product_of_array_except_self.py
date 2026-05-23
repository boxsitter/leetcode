# ID: 238 | Product of Array Except Self
# URL: https://leetcode.com/problems/product-of-array-except-self/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The naive approach is obviously to iterate through the array for each value in answer, keeping a running total and multiplying each value skipping num[i]
        # But I can't even do the naive approach because the problem required O(n) time
        # My second idea would be to get the product of all values and divide for each answer value but division is banned

        left_prod = [0] * len(nums)
        right_prod = [0] * len(nums)
        answer = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                left_prod[i] = 1
                right_prod[len(nums) - 1] = 1
            else:
                left_prod[i] = nums[i - 1] * left_prod[i - 1]
                right_prod[len(nums) - i - 1] = nums[len(nums) - i] * right_prod[len(nums) - i]

        for i in range(len(nums)):
            answer[i] = left_prod[i] * right_prod[i]

        return answer

        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    from test_case_runner import run_tests
    run_tests(Solution(), """
Test Case 1:
-----------------------------------------------------
input:
[1,2,3,4]
-----------------------------------------------------
expected output:
[24,12,8,6]

Test Case 2:
-----------------------------------------------------
input:
[-1,1,0,-3,3]
-----------------------------------------------------
expected output:
[0,0,9,0,0]""")