class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        val=''
        for i in letters:
            if target <i:
                val=i
                break
        if not val:
            return letters[0]
        return val