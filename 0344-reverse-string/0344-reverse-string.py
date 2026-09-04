class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = []
        for i in s:
            st.append(i)
            

        for j in range(len(s)):
             a = st.pop()
             s.append(a)
             s.pop(0)
        