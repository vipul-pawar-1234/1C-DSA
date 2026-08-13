def smallest_window(s, t):
    smallest = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            window = s[i:j]
            found = True

            for ch in t:
                if ch not in window:
                    found = False
                    break

            if found:
                if smallest == "" or len(window) < len(smallest):
                    smallest = window

    return smallest

s = "ADOBECODEBANC"
t = "CODB"
print(smallest_window(s, t))