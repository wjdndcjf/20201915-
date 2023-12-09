#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201915 이름 : 정우철

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution1(my_strung, target):
    if target in my_strung:    # in 키워드 문자열의 존재여부에 따라 bool 값 반환
        return 1;              # 존재하면 1 리턴
    else:
        return 0;              # 존재하지 않으면 0 리턴

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution2(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''
    for i in letter.split():             # 공백 기준으로 letter을 분리후 반복
        if i in morse:                   # i가 morse에 존재 여부 확인
            answer = answer + morse[i]   # 존재하면 문자열에 연결
        else:                            # i가 morse에 존재하지 않으면
            return "error"               # 잘못된 입력이므로 error 리턴
    return answer

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution3(age):
    ageDic = {
        "0":"a", "1":"b", "2":"c", "3":"d", "4":"e",
        "5":"f", "6":"g", "7":"h", "8":"i", "9":"j"}  # 숫자랑 알파벳 딕셔너리 생성
    answer = ''
    for i in str(age):                 # age를 문자열로 형변환 후 한글자씩 반복
        answer = answer + ageDic[i]    # 대응 되는 알파벳으로 문자열 연결
    return answer

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution4(r1, r2):
    max = r2 + 1                        # r2가 더 크므로 r2 기준으로 최대 범위 결정
    min = -r2                          # 최소 범위 결정
    answer = 0
    for x in range(min, max):           # x좌표 반복
        for y in range(min, max):       # y좌표 반복
            len = (x**2 + y ** 2)** 0.5 # 피타고라스로 점의 길이 도출
            if( r2 >= len >= r1 ):      # 길이가 r2와 r1 사이면 두원 사이에 존재하므로
                answer += 1             # 정답 1 증가
    return answer

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution5(numbers):
    # 수는 윗자리에 큰 수가 들어갈 수록 커지므로 최대한 윗자리에 큰 수가 오도록
    # 정렬한다.
    numbers.sort(key=lambda x : (str(x)[0],                             # 첫재짜리 비교
                                 str(x)[0] if x < 10   else str(x)[1],  # 첫째짜리가 같으면 둘째짜리 비교 둘째짜리가 없으면 첫재짜리로 비교
                                 str(x)[0] if x < 100  else str(x)[2],  # 둘째짜리가 같으면 셋째짜리 비교 셋째짜리가 없으면 첫재짜리로 비교
                                 str(x)[0] if x < 1000 else str(x)[3]), # 셋째짜리가 같으면 넷째짜리 비교 넷째짜리가 없으면 첫재짜리로 비교
                                 reverse = True)
    answer = ''
    for i in numbers:
        answer = answer + str(i)
    return answer
