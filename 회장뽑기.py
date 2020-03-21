import sys
sys.stdin = open("input.txt","r")
if __name__=="__main__":
    n=int(input())
    dis=[[100]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dis[i][i]=0
    while True:
        a,b=map(int,input().split())
        if a==-1 and b==-1
            break
        dis[a][b]=1
        dis[b][a]=1

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dis[i][j]=min(dis[i][j],)