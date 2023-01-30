def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer

'''
programmers lv0 코딩테스트 입문 이진수 더하기
이진수를 의미하는 두개의 문자열 bin1과 bin2의 합을 return하시오

ex.
bin1 = "10"
bin2 = "11"
result = "101"

bin1 = "1001"
bin2 = "1111"
result = "11000"

int('문자열', 2) -> 문자열을 이진수값으로 인식해서 int로 변환
'''