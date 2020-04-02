def hanoi(num,start,to,mid,answer):
    if num==1:
        return answer.append([start,to])
        
    hanoi(num-1,start,mid,to,answer)
    answer.append([start,to])
    hanoi(num-1,mid,to,start,answer)
        
        
def solution(n):
    answer = []
    hanoi(n,1,3,2,answer)
    return answer
