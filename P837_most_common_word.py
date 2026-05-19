# ID: 837 | Most Common Word
# URL: https://leetcode.com/problems/most-common-word/

from typing import List, Optional
from collections import Counter


#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        clean_paragraph = "".join(char if char.isalnum() else " " for char in paragraph).lower()
        words = clean_paragraph.split()
        counts = Counter(words)
        for word in banned:
            counts.pop(word, None)
        greatest_count = 0
        output = ""
        for word in counts:
            if counts[word] > greatest_count:
                greatest_count = counts[word]
                output = word
        return output
        
#IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == "__main__":
    sol = Solution()
    print(sol.mostCommonWord("This is a test for this function. It is a good function, this one.", ["this"]))
    print("--- Local Run Complete ---")