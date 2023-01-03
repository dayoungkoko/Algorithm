n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse= True)
cnt, result = 0, 0
for _ in range(m) :
    if (cnt % k == 0) and (cnt!=0) :
        result += lst[1]
        cnt+=1
    else : 
        result += lst[0]
        cnt += 1
print(result)



#### 정답 코드
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# first = data[n-1]
# second = data[n-2]
# result = 0
# while True :
#     for i in range(k) :
#         if m==0 : 
#             break
#         result += first
#         m-=1
#     if m== 0 :
#         break
#     result += second
#     m-=1

# print(result)