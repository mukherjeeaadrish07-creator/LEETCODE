class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        lst = []
        max = 0
        for i in sentences:
            lst = i.split()
            if len(lst)> max:
                max = len(lst)
        return max
