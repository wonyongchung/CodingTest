import sys
sys.stdin = open("input.txt",'r')
n=int(input())
house = list(map(int,input().split()))
k=int(input())

for i in range(k):
    house.sort()
    house[0]=house[0]+1
    house[n-1]=house[n-1]-1
house.sort()
cnt=house[n-1]-house[0]
print(cnt)