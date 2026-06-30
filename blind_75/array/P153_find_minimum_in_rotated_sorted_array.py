# ID: 153 | Find Minimum in Rotated Sorted Array
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # I am going to try iterating forward until I find the end
        # I'll know this because it's the first number that is less than the one before

        # for i in range(len(nums)):
        #     if i == len(nums) - 1:
        #         return nums[0]
        #     elif nums[i + 1] < nums [i]:
        #         return nums[i + 1]
        # return 0

        # This works but it's O(n), not O(Log n)
        # Need to do binary search
        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:
                # search right
                left = mid + 1
            else:
                # search left
                right = mid - 1

        return result



        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    from test_case_runner import run_tests
    run_tests(Solution(), """
Test Case 1:
-----------------------------------------------------
input:
[3,4,5,1,2]
-----------------------------------------------------
expected output:
1

Test Case 2:
-----------------------------------------------------
input:
[4,5,6,7,0,1,2]
-----------------------------------------------------
expected output:
0

Test Case 3:
-----------------------------------------------------
input:
[11,13,15,17]
-----------------------------------------------------
expected output:
11""")