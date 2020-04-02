def solution(people, limit):
    answer = 0
    people.sort()
    light=0
    heavy=len(people)-1
    while light<=heavy:
        if people[light]+people[heavy]<=limit:
            answer+=1
            light+=1
            heavy-=1
        else:
            answer+=1
            heavy-=1
    return answer
