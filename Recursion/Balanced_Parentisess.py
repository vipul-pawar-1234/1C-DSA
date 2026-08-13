def generate(s,open,close,n):
    if len(s) == 2*n:
        print(s)
        return
    
    if open<n:
        generate(s+"(",open+1,close,n)

    if close<open:
        generate(s+")",open,close+1,n)
    

generate("",0,0,3)