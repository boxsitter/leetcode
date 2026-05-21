# ID: 53 | Maximum Subarray
# URL: https://leetcode.com/problems/maximum-subarray/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Naive method is to calculate the sum of every possible subarray and return the max
        # max_value = None
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i, len(nums)):
        #         count += nums[j]
        #         if max_value is None or count > max_value:
        #             max_value = count
        # return max_value

        max_subarray_sum = nums[0]
        temp_sum = 0

        for item in nums:
            if temp_sum < 0:
                temp_sum = 0
            temp_sum += item
            max_subarray_sum = max(max_subarray_sum, temp_sum)
        return max_subarray_sum
        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    # To test locally, uncomment the lines below:
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print("--- Local Run Complete ---")