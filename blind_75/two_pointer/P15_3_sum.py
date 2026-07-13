# ID: 15 | 3Sum
# URL: https://leetcode.com/problems/3sum/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # This works but it is a mess and wildly inneficient
        # i = 0
        # j = 1
        # k = 2
        # results = []
        #
        # while i != len(nums) - 3:
        #     if nums[i] + nums[j] + nums[k] == 0:
        #         triplet = [nums[i], nums[j], nums[k]]
        #         triplet.sort()
        #         if triplet not in results:
        #             results.append(triplet)
        #
        #     if k + 1 != len(nums):
        #         k += 1
        #     elif j + 1 != k:
        #         j += 1
        #         k = j + 1
        #     elif i + 1 != k:
        #         i += 1
        #         j = i + 1
        #         k = j + 1
        #
        # if nums[i] + nums[j] + nums[k] == 0:
        #     triplet = [nums[i], nums[j], nums[k]]
        #     triplet.sort()
        #     if triplet not in results:
        #         results.append(triplet)
        #
        # return results

        # i < j < k
        i = 0
        j = 1
        k = 2
        results = []

        nums.sort()

        while i < j:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum < 0:
                    j += 1
                elif current_sum > 0:
                    k -= 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    results.append(triplet)
                    j += 1
                    while j < len(nums) - 1 and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            # dupe prevention
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return results

        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    from test_case_runner import run_tests
    run_tests(Solution(), """
Test Case 1:
-----------------------------------------------------
input:
[-1,0,1,2,-1,-4]
-----------------------------------------------------
expected output:
[[-1,-1,2],[-1,0,1]]

Test Case 2:
-----------------------------------------------------
input:
[0,1,1]
-----------------------------------------------------
expected output:
[]

Test Case 3:
-----------------------------------------------------
input:
[0,0,0]
-----------------------------------------------------
expected output:
[[0,0,0]]

Test Case 4:
-----------------------------------------------------
input:
[2,0,-2,-5,-5,-3,2,-4]
-----------------------------------------------------
expected output:
[[-4,2,2],[-2,0,2]]""")