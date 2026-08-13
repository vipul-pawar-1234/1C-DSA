def isValid(str):
    stack = []
    mapping = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for char in str:
        if char in mapping:
            
            if stack:
                top = stack[-1]
                stack = stack[:-1]
            else:
                top = 'n'

            if mapping[char] != top:
                return False
        else:
            stack = stack + [char]
    
    bool = len(stack) == 0

    return bool


str = "{[()]}"

if isValid(str):
    print("All Paranthises are same")
else:
    print("Not Same")