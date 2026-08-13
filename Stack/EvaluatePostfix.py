def evaluatePostfix(arr):
    stack = []

    for ch in arr:

        if ch not in "+-/*":
            stack = stack + [ch]

        else:
            top = stack[-1]
            stack = stack[:-1]
            num1 = int(top)

            top = stack[-1]
            stack = stack[:-1]
            num2 = int(top)

            if ch == "+":
                stack = stack +[num1+num2]
            
            if ch == "-":
                stack = stack + [num1-num2]
            
            if ch == "*":
                stack = stack + [num2*num1]
            
            if ch == "//":
                stack = stack + [num2 // num1]
            
    return stack

arr = ["6","2","8","*","+"]
result = evaluatePostfix(arr)
print("Stack is:",result)

