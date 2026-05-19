# ID: 125 | Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Plan: I am going to iterate through the string, checking if index i == len(s) - i
        # Just not sure when to stop the loop? len(s) // 2 maybe?
        lowercase_s = s.lower()
        clean_s = "".join(char for char in lowercase_s if char.isalnum())
        for i in range(len(clean_s) // 2):
            if clean_s[i] != clean_s[len(clean_s) - i - 1]:
                return False
        return True

        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print("--- Local Run Complete ---")