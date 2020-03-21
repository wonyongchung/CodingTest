import sys
sys.stdin = open("input.txt","r")

def DFS(L,sum):
    global cnt
    if sum>n:
        return
    if L==m:
        if sum==n:
            cnt+=1
    else:
        for i in range(b[L]+1):
            DFS(L+1,sum+(i*a[L]))


if __name__=="__main__":
    n=int(input())  #지불 가격
    m=int(input())  #동전 종류
    a=[]   #동전종류 리스트
    b=[]   #동전갯수 리스트

    for _ in range(m):
        c,d=map(int,input().split())
        a.append(c)
        b.append(d)
    cnt=0
    DFS(0,0)
    print(cnt)