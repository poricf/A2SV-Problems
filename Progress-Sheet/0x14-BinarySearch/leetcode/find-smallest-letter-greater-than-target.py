class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = bisect_left(letters,target)

        if left < len(letters):
            if letters[left] == target:
                right = bisect_right(letters,target)
                if right < len(letters):
                    return letters[right]
            else:
                return letters[left]
        
        return letters[0]