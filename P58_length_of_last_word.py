# ID: 58 | Length of Last Word
# URL: https://leetcode.com/problems/length-of-last-word/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Plan: Going to try to parse the string into an array of words and return len(words[-1])
        words = s.split()
        return len(words[-1])
        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    # To test locally, uncomment the lines below:
    # print(sol.findMedianSortedArrays([1, 3], [2]))
    print("--- Local Run Complete ---")