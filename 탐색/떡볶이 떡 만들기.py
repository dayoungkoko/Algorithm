n, m = map(int, input().split())
arr = list(map(int, input().split()))

def tteokbbokki(array, target, start, end) :
    while start<= end : 
        mid = (start+end)//2
        length = 0
        for elem in arr :
            if elem>=mid : 
                length += elem-mid
        if length == target :
            return mid
        elif length < target :
            end-=1
        else :
            start+=1

start, end = min(arr), max(arr)
answer = tteokbbokki(arr, m, start, end)
print(answer)

'''
이진 탐색 응용 문제
이것이 코딩테스트다 p.201> 실전문제3. 떡볶이 떡 만들기
절단기에 설정할 수 있는 높이의 최대값을 구하는 프로그램

입력 예시.
4 6
19 15 10 17

출력 예시.
15
'''