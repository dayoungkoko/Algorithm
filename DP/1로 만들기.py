x = int(input())

d = [0]*30001

for i in range(2,x+1) :
    d[i] = d[i-1]+1
    
    if i%2 == 0 :
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0 :
        d[i] = min(d[i], d[i//3]+1)
    if i%5 == 0 :
        d[i] = min(d[i], d[i//5]+1)
        
print(d[x])

'''
이것이 코딩테스트다 p.217 1로 만들기
연산을 사용하는 횟수의 최솟값 구하기

입력 예시> 26
출력 예시> 3
'''