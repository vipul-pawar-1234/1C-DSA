def infixToPrefix(arr):
    stack = []
    result = ""

    for ch in arr:
        if 'A' <= ch <= 'Z':
            result += ch
        
        elif ch in "+-":
            while stack:
                top = stack[-1]
                stack = stack[:-1]
                result += top
            stack = stack + [ch]

        elif ch in "*/":
            stack = stack + [ch]
        
    while stack:
            top = stack[-1]
            stack = stack[:-1]
            result += top

    return result


print(infixToPrefix("A+B*C"))



            
        