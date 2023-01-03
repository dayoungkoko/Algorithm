n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
second = data[1]
repeated= first*k + second
result = repeated*(m//(k+1)) + first*(m%(k+1))
print(result)