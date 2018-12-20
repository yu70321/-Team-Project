def mispelling(n, text):
    """
    :param n: 입력된 자연수
    :param text: 입력된 문자
    """
    ss= ''
    for a in range(len(text)):
        if a == n-1:
            text.replace(text[a] ,"")
        else:
            ss += text[a]
    ''' for문을 이용해서 입력한 자연수-1 랑 인덱스값을 비교하여 
    그 찾은 값이 맞으면 replace를 이용하여 ""칸으로 만들고
    문자를 합친다.'''

    return ss



