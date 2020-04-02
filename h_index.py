def solution(citations):
    answer = 0
    a=max(citations)
    b=len(citations)
    tmp1=0
    tmp2=0
    for i in range(a+1):
        for j in range(b):
            if citations[j]>=i:
                tmp1+=1
            if citations[j]<=i:
                tmp2+=1
        if tmp1==tmp2:
            answer=i
            break
        else:
            tmp1=0
            tmp2=0
    return answer
