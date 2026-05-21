# ID: 387 | First Unique Character in a String
# URL: https://leetcode.com/problems/first-unique-character-in-a-string/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        indices = {}
        for index, char in enumerate(s):
            if char in counts:
                counts[char] = counts[char] + 1
            else:
                counts[char] = 1
                indices[char] = index
        for key in list(counts.keys()):
            if counts[key] == 1:
                return indices[key]
        return -1


#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcodes"))
    print("--- Local Run Complete ---")