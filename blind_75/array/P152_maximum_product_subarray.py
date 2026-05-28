from typing import List


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Naive method is to calculate every subarray product
        # I am going to try to implement the strategy from maximum subarray from memory
        # That won't work because negative values aren't necessarily non-beneficial

        # I am going to keep two running products
        # An optimistic product assumes there will always be another negative and only resets on zeros
        # A pessimistic product assumes there will NOT be another negative and resets on negatives and zeros
        # The running max value will be the maximum between itself, the optimistic product, and the pessimistic product
        # This works because all three values will always be valid subarray products, and once the array has been iterated through, one is guaranteed to be correct

        # max_product = nums[0]
        # optimistic_running_product = 1
        # pessimistic_running_product = 1
        # for num in nums:
        #     if num < 0:
        #         optimistic_running_product *= num
        #         pessimistic_running_product = 1
        #     elif num > 0:
        #         optimistic_running_product *= num
        #         pessimistic_running_product *= num
        #     else: # num is zero
        #         optimistic_running_product = 0
        #         pessimistic_running_product = 0
        #
        #     max_product = max(max_product, optimistic_running_product, pessimistic_running_product, num)
        #
        # return max_product

        # Didn't work out

        # Dad's solution

        # maximum = nums[0]
        # running_positive = 0
        # running_negative = 0
        # running_positive_set = False
        # running_negative_set = False
        #
        # for num in nums:
        #     swap = False
        #     if num < 0 and not running_negative_set:
        #         running_negative = num
        #         running_negative_set = True
        #     elif running_negative_set:
        #         running_negative *= num
        #         if num < 0:
        #             swap = True
        #
        #
        #     if num > 0 and not running_positive_set:
        #         running_positive = num
        #         running_positive_set = True
        #     elif running_positive_set:
        #         running_positive *= num
        #         if num > 0:
        #             swap = True
        #
        #     if num == 0:
        #         running_positive = 0
        #
        #     if num < 0 and swap:
        #         # swap running_positive and running_negative
        #         temp = running_positive
        #         running_positive = running_negative
        #         running_negative = temp
        #
        #         temp = running_positive_set
        #         running_positive_set = running_negative_set
        #         running_negative_set = temp
        #
        #     if running_positive_set:
        #         maximum = max(running_positive, maximum)
        #
        #     if num == 0:
        #         running_positive_set = False
        #         running_negative_set = False
        #
        # return maximum

        # at every element, I need to know both the maximum and minimum product of any subarray ending at that element


        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    from test_case_runner import run_tests

    run_tests(Solution(), """
Test Case 1:
-----------------------------------------------------
input:
[2,3,-2,4]
-----------------------------------------------------
expected output:
6

Test Case 2:
-----------------------------------------------------
input:
[-2,0,-1]
-----------------------------------------------------
expected output:
0

Test Case 3:
-----------------------------------------------------
input:
[-3,-1,-1]
-----------------------------------------------------
expected output:
3

Test Case 4:
-----------------------------------------------------
input:
[-2]
-----------------------------------------------------
expected output:
-2

Test Case 5:
-----------------------------------------------------
input:
[-5,0]
-----------------------------------------------------
expected output:
0""")