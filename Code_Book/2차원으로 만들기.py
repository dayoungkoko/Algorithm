def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer


def solution2(num_list, n) :
    answer = [[]] * (len(num_list)//n)
    for cal in range(len(num_list)//n) :
        result = []
        for idx in range(len(num_list)) :
            if idx//n == cal :
                result.append(num_list[idx])
        answer[cal] = result
    return result




'''
programmers lv.0 코딩테스트 입문 2차원으로 만들기
정수 배열 num_list와 정수 n이 매개변수로 주어질 때, 다음과 같이 num_list를 2차원 배열로 바꿔 return 하시오

ex.
num_list = [1,2,3,4,5,6,7,8]
n = 2
result = [[1,2],[3,4],[5,6],[7,8]]

ex.
num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
n = 3
result = [[100, 95, 2], [4,5,6], ,[18,33,948]]

'''