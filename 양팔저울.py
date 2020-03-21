import sys
sys.stdin = open("input.txt", "r")

def DFS(L,sum):
    global res
    if L==n:
        if 0<sum<=total:
            res.add(sum)
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum-a[L])
        DFS(L+1,sum)

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total=sum(a)
    res=set()
    DFS(0,0)
    print(total-len(res))


