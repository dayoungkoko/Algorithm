n, m = map(int, input().split())
arr = list()
for _ in range(n) :
    arr.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
for i in range(n) :
    for j in range(arr[i], m+1) :
        if d[j - arr[i]] != 10001 :
            d[j] = min(d[j], d[j-arr[i]]+1)
            
if d[m] == 10001 :
    print(-1)
else :
    print(d[m])

'''
이것이 코딩테스트다 p.226 효율적인 화폐 구성

입력 예시1>
2 15
2
3

출력 예시1>
5

입력 예시2>
3 4
3
5
7

출력 예시2>
-1
'''