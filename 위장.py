from collections import Counter
def solution(clothes):
    answer = 0
    mycollection=Counter([cat for _, cat in clothes])
    all_possible=1
    
    for key in mycollection:
        all_possible*=(mycollection[key]+1)
    
    return all_possible-1
