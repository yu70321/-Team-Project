print("원하시는 음식종류를 입력하세요.(한식, 중식, 양식)")
# step1. 음식 종류 입력받기
a = input()

print("서울지역을 입력하세요.(영등포구, 강서구 등 '구'단위)")
# step2. 음식 종류에 대한 지역 입력받으면 해당 지역에 대한 맛집이름 불러오기
w = input()


""" csv 파일을 입력 받아올 수 있도록 import 한 뒤
    'a' 값으로 입력받은 음식종류 파일을 찾아 오픈 후 해당 파일 내
    입력 받았 던 'b' 지역에 대한 맛집이름을 불러올 수 있도록
    csv 입력내용을 list에 저장 후 dictionary로 변환시켜준다. """

import csv
with open(a + ".csv", 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    result = [line for line in csv_reader]
    result = result[1:]  # 지역:맛집 으로 리스트 생성
    restaurant_dict = dict(result)  # 리스트 딕셔너리 변환
    s = restaurant_dict[w]   # 맛집이름 저장
    print('추천맛집: ' + s)

""" 입력 받은 's' 맛집이름을 기준값 으로 맛집정보를 불러올 수 있는
    url 정보가 기재 된 c 파일을 다시 입력 받은 뒤 또 다른 dictionary 생성.
    's' 맛집이름에 해당되는 web data를 추출할 수 있도록 requests, BeaurifulSoup import."""

print("해당 맛집에 대한 전화번호와 정보를 안내해드리겠습니다.")
import requests
from bs4 import BeautifulSoup

with open("맛집정보.csv", 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    result2 = [line for line in csv_reader]
    result2 = result2[1:]  # 맛집:URL 리스트 생성
    review = dict(result2)  # 리스트 딕셔너리 변환
    m = review[s]

    url = review[s]  # 위에서 입력받은 맛집에 해당된 url 출력
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    restaurant_result = soup.find('div', class_='p_tel') # 전화번호를 가져오기 위한 해당 class 출력

    for s in restaurant_result.find_all('p'):
        print("전화번호: "+s.text)
        print("맛집정보: " + m)
