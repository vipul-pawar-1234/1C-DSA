def macthing(text , pattarn):
    n = len(text)
    m = len(pattarn)

    for i in range (n - m + 1):
        window = text[i:i+m]

        if hash(window) == hash(pattarn):
            if window == pattarn:
                print("Position found at:",i)

macthing("ABCCDDAEFG","CDD")