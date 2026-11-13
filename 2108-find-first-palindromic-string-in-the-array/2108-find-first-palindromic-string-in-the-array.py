class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        lst = []
        for i in words:
            if i[::-1] == i:
                lst.append(i)
        
        if not lst :
            return("")
        else:
            return(lst[0])
