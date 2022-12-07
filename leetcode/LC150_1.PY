def evalRPN(tokens):
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return stack.pop()
    
    
a= evalRPN(["2","1","+","3","*"])
# print(a)   