class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i = 0
        for ele in pushed:
            stk.append(ele)

            while stk and i < len(popped) and stk[-1] == popped[i]:
                stk.pop()
                i+=1
        

        return not stk