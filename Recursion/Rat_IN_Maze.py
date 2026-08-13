def solve(maze,visite,i,j,path):
    n = len(maze)

    if i<0 or j<0 or i>=n or j>=n:
        return
    
    if maze[i][j] == 0:
        return
    
    if visite[i][j]:
        return
    
    if i == n-1 and j == n-1:
        print(path)
        return
    
    visite[i][j] = True
    
    solve(maze,visite,i+1,j,path+"D")
    solve(maze,visite,i,j+1,path+"R")
    solve(maze,visite,i,j-1,path+"L")
    solve(maze,visite,i-1,j,path+"U")

    visite[i][j] = False

maze = [
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1]
]
visite = [
    [False,False,False,False,False],
    [False,False,False,False,False],
    [False,False,False,False,False],
    [False,False,False,False,False],
    [False,False,False,False,False],
]

solve(maze,visite,0,0,"")