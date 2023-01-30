def solution(numbers, k):
    if len(numbers) % 2 == 0 :
        lst = [i for i in range(1,len(numbers)+1) if i%2 != 0]
        return lst[k%(len(numbers)//2)-1]
    else :
        lst = [i for i in range(1,len(numbers)+1) if i%2 != 0] + [i for i in range(1,len(numbers)+1) if i%2 == 0]
        return lst[k%len(numbers)-1]
    
def solution2(numbers, k) :
    return numbers[2 * (k - 1) % len(numbers)]

'''
programmers lv.0 코딩테스트 입문 공 던지기
공은 1번부터 던지며 오른쪽으로 한명씩 건너뛰고 그 다음 사람에게만 던진다.
친구들의 번호가 들어있는 정수 배열 numbers, 정수 k가 주어질 때
k번째로 공을 던지는 사람의 번호는?

ex.
numbers = [1,2,3,4]
k = 2
result = 3

numbers = [1,2,3,4,5,6]
k = 5
result = 3

numbers = [1,2,3]
k = 3
result = 2
'''