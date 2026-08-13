def largestRactangle(height):
    stack = []
    max_area = 0
    height = height + [0]

    for i in range (len(height)):
        while stack and height[i] < height[stack[-1]]:
            top = stack[-1]
            stack = stack[:-1]
            h = height[top]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = h*width
            max_area = max(area,max_area)
        
        stack = stack + [i]
    return max_area

height = [2,1,5,6,2,3]
print(largestRactangle(height))