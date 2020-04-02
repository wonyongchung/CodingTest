def gcd(n,m):
    while m:
        n,m=m,n % m
    return n
 
def solution(w,h):
    l=gcd(w,h)
    entire=w*h
    return entire -l*((w//l)+(h//l)-1)
