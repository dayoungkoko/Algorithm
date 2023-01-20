def solution(array) :
    from collections import Counter
    counter = dict(Counter(array))
    answer = [k for k,v in counter.items() if v == max(list(counter.values()))]
    if len(answer) > 1 :
        return -1
    else :
        return answer[0]

'''
programmers 코딩테스트 입문 lv.0 최빈값 구하기
정수 배열 array가 매개변수로 주어질 때 최빈값을 return하도록 solution함수를 완성하세요
만약 최빈값이 여러개면 -1을 return합니다.

풀이 : 
'원소'를 key로, '원소의 개수'를 value값으로 하는 dictionary로 변환하여 
가장 큰 value값을 갖는 key값을 반환한다

ex :
array = [1,2,3,3,3,4]
result = 3

array = [1,1,2,2]
result = -1

array = [1]
result = 1
'''
