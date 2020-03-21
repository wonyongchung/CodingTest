x=  int(input("수를 입력하세요"))
y=  int(input("몇번째 약수를 원하는지 입력하세요"))
z=0  #약수의 개수
list=[]

for i in range (1,x+1):
    if x%i==0:
        z=z+1
        list.append(i)

if y>z:
    print("약수의 개수가 부족합니다")

print(list[y-1])




