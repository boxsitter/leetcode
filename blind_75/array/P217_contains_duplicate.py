# ID: 217 | Contains Duplicate
# URL: https://leetcode.com/problems/contains-duplicate/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # My immediate instinct is to use a hashmap to with array items as keys and counts as values
        # On second thought, it would be better to create a set of seen values and simply check if a new value is contained within the set
        # seen = set()
        # for value in nums:
        #     if value in seen:
        #         return True
        #     seen.add(value)
        # return False

        # Second idea, add all elements of nums to a set and check if the lengths are the same
        nums_as_set = set()
        nums_as_set.update(nums)
        if len(nums_as_set) == len(nums):
            return False
        else:
            return True

        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    # To test locally, uncomment the lines below:
    # print(sol.findMedianSortedArrays([1, 3], [2]))
    print("--- Local Run Complete ---")