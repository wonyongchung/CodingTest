import sys
sys.stdin = open("input.txt","r")
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y):
    global cnt
    if x==n-1 and y==n-1:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if a[xx][yy]>a[x][y]:
                tmp=a[xx][yy]
                a[xx][yy] = 0
                DFS(xx,yy)
                a[xx][yy]=tmp


if __name__=="__main__":
    n=int(input())
    a=[list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    a[0][0]=0
    DFS(0,0)