import sys
sys.stdin = open("input.txt","r")

def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]

if __name__=="__main__":
    n=int(input())
    res=2147000000
    coin=[]
    for _ in range(n):
        coin.append(int(input()))
    money=[0]*3
    DFS(0)
    print(res)