# ID: 33 | Search in Rotated Sorted Array
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # I'm just going to try to alter the "find minimum" code to move towards the target val
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # If mid and target are in the same section of the sorted array: search right if target is greater than mid
            # If mid and target are in different sections: search right if mid is in the left section
            # if ((nums[mid] >= nums[left]) == (target >= nums[left])) and nums[mid] <= target:
            #     # search right
            #     left = mid + 1
            # elif ((nums[mid] >= nums[left]) != (target >= nums[left])) and nums[mid] >= nums[left]:
            #     # search right
            #     left = mid + 1
            # else:
            #     # search left
            #     right = mid - 1

            # Simplified logic:
            # If the left half is sorted (nums[left] <= nums[mid]):
                # If target is in [nums[left], nums[mid]) → search left
                # Otherwise → search right
            # Otherwise the right half is sorted:
                # If target is in (nums[mid], nums[right]] → search right
                # Otherwise → search left
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    # search left
                    right = mid - 1
                else:
                    # search right
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    # search right
                    left = mid + 1
                else:
                    # search left
                    right = mid - 1
        return -1

#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    from test_case_runner import run_tests
    run_tests(Solution(), """
Test Case 1:
-----------------------------------------------------
input:
[4,5,6,7,0,1,2]
0
-----------------------------------------------------
expected output:
4

Test Case 2:
-----------------------------------------------------
input:
[4,5,6,7,0,1,2]
3
-----------------------------------------------------
expected output:
-1

Test Case 3:
-----------------------------------------------------
input:
[1]
0
-----------------------------------------------------
expected output:
-1

Test Case 4:
-----------------------------------------------------
input:
[4,5,6,7,0,1,2]
5
-----------------------------------------------------
expected output:
1

Test Case 5:
-----------------------------------------------------
input:
[8,1,2,3,4,5,6,7]
6
-----------------------------------------------------
expected output:
6""")