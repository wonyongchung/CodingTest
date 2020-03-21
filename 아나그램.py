import sys
sys.stdin = open("input.txt","r")
a=input()
b=input()
str1=dict()
str2=dict()
for x in a:
    str1[x]=str1.get(x,0)+1
for x in b:
    str2[x]=str2.get(x,0)+1

if str1==str2:
    print("YES")
else:
    print("NO")