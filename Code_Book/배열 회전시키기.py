def solution(numbers, direction) :
    return [numbers[-1]] + numbers[:-1] if direction== 'right' else numbers[1:] + [numbers[0]]

'''
programmers 코딩테스트 입문 lv.0 배열 회전시키기 문제
numbers의 원소를 direction 방향으로 한 칸씩 회전시킨 배열을 return 한다.

ex.
numbers = [1,2,3]
direction = 'right'
result = [3,1,2]

numbers = [4,455,6,4,-1,45,6]
direction = 'left'
result = [455, 6, 4, -1, 45, 6, 4]

풀이.
내 풀이 >
'''
def solution2(numbers, direction):
    answer = [1]*len(numbers)
    for idx in range(len(numbers)) :
        if direction == 'right' :
            answer[idx] = numbers[idx-1]
        else :
            if idx+1 >= len(numbers) :
                index = 0
            else :
                index = idx+1
            answer[idx] = numbers[index]
    return answer
'''
간단한 풀이 >
문자열 인덱싱
'''