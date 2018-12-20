
""" 이화정(2017053154), 전은영(2017053209) """

def caesar(plaintext):
    bb = plaintext
    # 받은 값을 bb라는 변수로 텍스트를 저장
    홀 = ''
    짝 = ''
    # 홀,짝 빈값을 만들어준다.

    for a in range(len(plaintext)) :
        if a % 2 == 0 :
            홀 += bb[a]
        else:
            짝 += bb[a]
    """ for문 이용하여 입력값(plaintext)의 길이까지 
    돌면서 홀짝을 나눠 각각 해당값을 저장해준다. """

    hap = 홀+짝
    # 각각 저장해 놓은 값을 합쳐준다.

    return hap



