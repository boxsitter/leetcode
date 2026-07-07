# ID: 20 | Valid Parentheses
# URL: https://leetcode.com/problems/valid-parentheses/

from typing import List, Optional


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def isValid(self, s: str) -> bool:
        # This works but its confusing and ugly

        # opening = ["(", "{", "["]
        # closing = [")", "}", "]"]
        # stack = []
        #
        # for char in s:
        #     if char in opening:
        #         stack.append(char)
        #     elif len(stack) == 0 or char in closing and char != closing[opening.index(stack.pop())]:
        #         return False
        #
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False

        matching = {")": "(", "}": "{", "]": "[",}
        stack = []
        for char in s:
            if char in matching:
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    from test_case_runner import run_tests
    run_tests(Solution(), """
Test Case 1:
-----------------------------------------------------
input:
"()"
-----------------------------------------------------
expected output:
true

Test Case 2:
-----------------------------------------------------
input:
"()[]{}"
-----------------------------------------------------
expected output:
true

Test Case 3:
-----------------------------------------------------
input:
"(]"
-----------------------------------------------------
expected output:
false

Test Case 4:
-----------------------------------------------------
input:
"([])"
-----------------------------------------------------
expected output:
true

Test Case 5:
-----------------------------------------------------
input:
"([)]"
-----------------------------------------------------
expected output:
false""")