def solution(array, n) :
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer


def solution2(array, n):
    diff = abs(n - array[0])
    idx = 0
    for i in range(1,len(array)) :
        if abs(n-array[i]) < diff :
            diff = abs(n - array[i])
            idx = i
        elif abs(n-array[i]) == diff :
            if array[idx] > array[i] :
                idx = i
    return array[idx]    


'''
programmers lv.0 코딩테스트 입문 가까운 수
정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 해라
가장 가까운 수가 여러 개일 경우 더 작은 수를 return 

ex.
array = [3,10,28]
n = 20
result = 28

array = [10,11,12]
n = 13
result = 12

lambda 풀이.
sorted에서 key를 설정할 때 lambda함수를 사용하여 우선순위를 정해줄 수 있음에 주의
'''