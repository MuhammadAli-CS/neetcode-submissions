class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={"-","+","*","/"}
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue
            right=stack.pop()
            left=stack.pop()
            if token=='+': result=left+right
            elif token=='-':result = left-right
            elif token=='*': result=left*right
            elif token=='/': result=int(left / right)
            stack.append(result)
        return stack.pop()