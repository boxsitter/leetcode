from typing import List


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = nums[0]
        running_positive = 0
        running_negative = 0
        running_positive_set = False
        running_negative_set = False

        for num in nums:
            swap = False
            if num < 0 and not running_negative_set:
                running_negative = num
                running_negative_set = True
            elif running_negative_set:
                running_negative *= num
                if num < 0:
                    swap = True


            if num > 0 and not running_positive_set:
                running_positive = num
                running_positive_set = True
            elif running_positive_set:
                running_positive *= num
                if num > 0:
                    swap = True

            if num == 0:
                running_positive = 0

            if num < 0 and swap:
                # swap running_positive and running_negative
                temp = running_positive
                running_positive = running_negative
                running_negative = temp

                temp = running_positive_set
                running_positive_set = running_negative_set
                running_negative_set = temp

            if running_positive_set:
                maximum = max(running_positive, maximum)

            if num == 0:
                running_positive_set = False
                running_negative_set = False

        return maximum



        
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