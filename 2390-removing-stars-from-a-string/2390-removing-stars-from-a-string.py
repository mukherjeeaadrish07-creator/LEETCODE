class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            st.append(i)

            if i == "*":
               st.pop()
               st.pop()
        return "".join(st)