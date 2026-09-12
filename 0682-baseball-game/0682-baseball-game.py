class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        C = 0
        for i in range(len(operations)):
            if operations[i] == "C":
                st.pop()
            elif operations[i] == "D":
                st.append(2 * st[-1])
            elif operations[i] == "+":
                st.append(st[-1] + st[-2])
            else:
                st.append(int(operations[i]))

        for i in st:
            C = C + i

        return C