n, m = map(int, input().split())
lst = []
for _ in range(n) :
    data = list(map(int, input().split()))
    lst.append(min(data))
print(max(lst))