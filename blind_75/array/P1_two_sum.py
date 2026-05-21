# ID: 1 | Two Sum
# URL: https://leetcode.com/problems/two-sum/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The slowest way to solve this is by checking each integer against every other integer
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i , j]
        # return None

        # New idea, add each seen number to a dictionary with its value as a key and its index as a value
        # Iterate once through nums and check if the dictionary contains target - nums[i]
        # If so, return [i, dict[target - nums[i]]]
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [i, seen[target - nums[i]]]
            else:
                seen[nums[i]] = i
        return None


#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    # To test locally, uncomment the lines below:
    # print(sol.findMedianSortedArrays([1, 3], [2]))
    print("--- Local Run Complete ---")