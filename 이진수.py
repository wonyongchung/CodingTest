import sys
sys.stdin=open("input.txt","r")
def two(x):
    if x==0:
        return
    else:

        two(x // 2)
        print(x % 2, end='')

if __name__=="__main__":
    n=int(input())
    two(n)