import math

def solution(progresses, speeds):
    answer = []
    mylist = [math.ceil((100-a)/b) for a,b in zip(progresses,speeds)]
    first = 0
    for i in range(len(mylist)):
        if mylist[first]<mylist[i]:
            answer.append(i-first)
            first=i
    answer.append(len(mylist)-first)
    return answer
