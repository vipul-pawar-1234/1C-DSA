def KMPSerching(text , pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n-m+1):

        if text[i:i+m] == pattern:
            print("Position found at:",i)

KMPSerching("ABDADIAGFIAJ","DIAG")