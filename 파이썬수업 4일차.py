##중요함.
from random import random  
# print(random())

# [예제.1]
# from random import random # random 함수를 호출 (현재 작업중인 소스파일)
# from random import randint
# print(random())
# print(randint(10,50)) #프레임워크는 작업대 라이브러리 형태로 묶어둠. 프레임워크사용하는 목적은 가져다가 쓰면 개발속도가 빨라서 

# import random
# print(random.random()) # 0.0 ~ 1.0 미만의 임의의 값이 생성
# print(random.randint(10,50)) # 도트연산자 즉 .이라는녀석은 내가 지정한 녀석 속으로 들어간다.
# 내가 라이브러리에서 특정기능을 쓸거야 할때 쓰는 방법만 알면됨. 이미 만들어져있음.
# import 기능 가져다가 끌어오기만하면됨.
# 라이브러리 싸움 
# 작업에 시작점
# django를 잘하면  spring, sprong boot가 쉬워짐
# django는 웹 어플리케이션을 만드는게 메인

# import random
# for i in range(6):
#   print(random.randint(1,100))

# import random
# num = 1
# import random

# while True:
#   num = random.randint(1,100)
#   print(num)
#   if num == 50:
#     break

# from random import randint
# while True:
#   a = randint(1,15)  
#   b = randint(1,15)
#   c = randint(1,15)
#   if a !=b and a !=c and b !=c:
#     print(a,b,c)
#     break

# i <=50:
#       print(random.randist(1,50))
#       i+=1
# for i in range(6):
#   print(f"{i+1}")

#[ List ]

# - 데이터의 목록을 다루는 자료형
# - 리스트 안에는 어떠한 자료형이던지 넣어 사용할 수 있다.
# - 리스트를 정의할때에는 "[]"를 사용한다.
# - 리스트 내부의 특정 데이터의 접근하기 위해서는 index를 사용한다.
# [ 100, 200, 300, 400, 500 ]  #index를 사용해서 안에있는 내부값을 가져올수있다.
# [100, 1.123, "string"] #자료형 아무것도 몰라도 내부적으로 자기가 알아서 처리를해줌. #어떠한 자료형이던지 하나의 저장공간에 집어넣어서 사용가능

# [예제 2]
# lst = [1,2,3,4,5]     #index 0,1,2,3,4 양쪽값이 매핑 됨
# print(lst, type(lst))
# print(lst[0])
# print(lst[2])
# print(lst[6])

# list index out of range  <<Error
# 인덱스에 범위를 벗어남. 인덱스 번호 잘못지정한거임

# lst = [1,2,3,4,5,123,456,"ASD"]
# print(lst, type(lst))
# for val in lst:   # lst의 모든 값을 하나씩 val에 넣어 반복
#   print(val)
# lst[0] = 100      #lst <에 0번 index값을 100으로 교체하겠다. 
# print(lst[0]) 


# lst = [1,2,3,4,5,123,456,"ASD"]
# print(lst[-2])     #음수조건은 가장 마지막에 -1을 받기때문에 마지막 값 데이터가 필요할때 lst안에 -1를 넣으면 됨. 음수는 역순임.
# 456 출력됨

#범위 지정 1,2,3,4,5만 필요하다 할 때 index번호가져다가 하나하나 값을 가져올수도있지만 슬라이싱을 쓰면 됨 인덱스번호가 데이터와 데이터 사이사이에 있음
# 데이터를 나타날때 범위
# lst = [1,2,3,4,5,123,456,"ASD"]
# print(lst[0:-1])
#print(lst[:3])
#print(lst[5:])

# print(lst[:3]) 앞쪽을 생각했기때문에 0이 생략되어있다. 그래서 1~3이 출력
# 1~5까지 출력됨
# index 5시작점으로 7 까지 출력


# [List 복사]
# - 얇은 복사 : 원본 리스트의 주소값을 복사
# - 깊은 복사 : 원본 리스트의 데이터를 복사


#얇은 복사
# lst1 = [1,2,3]
# print(lst1,id(lst1))   #id라는건 저장공간 확인  lst1번이랑 lst2번이랑 값이 같음.
# lst2 = lst1  #메모리의 주소값을 복사 실질적으로 0x100번지라는 주소가 복사되어서 저장됨. 데이터를 하나 더 구현  
# print(lst2,id(lst2))

# lst2[0] = 100
# print(lst2)
# print(lst1)


#깊은 복사  #일반적인 복사를 하려면 깊은복사를 사용해야함. 웹에서 가져온 데이터를 스크래핑해서 저장할때 다이렉트로 하는게아님. 

#깊은복사
# from copy import copy
# lst1 = [1,2,3]                #주소가 비슷해보이지만 다름. 최대한 근접한 공간에 만든 프레임 영역을 근접한 특정영역에 잡아버림.
# print(lst1,id(lst1))   
# lst2 = copy(lst1)    
# print(lst2,id(lst2))

# lst2[0] = 100
# print(lst2)
# print(lst1)

#복사를 한다고 하면 copy모듈 함수를 써야겠구나 라는걸 기억하기
# [예제.4]
lst = [1,2,3]
print(lst)

lst.append(['A','B','C'])
print(lst)


#[예제.5]
# lst = [1,2,3]   
# print(lst)

# lst.extend([100,200,300]) #extend는 리스트 덩어리가 두개가 있을 때 하나의 리스트 덩어리로 합칠 때 사용 
# print(lst)

#[예제.6]
# lst = [1,2,3]
# lst.insert(1,'A') #값을 내가 추가 해야할 때 
# print(lst)

# # 값 삭제 함수 
# data = lst.pop(1)   # (추출) 리스트속에 있는 데이터를 가져와서 쓸건지
# print(lst, data)

# data2 = lst.remove(3)  # 그냥 삭제할것인지.
# print(lst, data2)

# lst.clear() #초기화
# print(lst)  

#[예제.7]
# lst = [1,2,3,'A','B','C','A']
# print(lst.count('A'))
# print(lst.index('A'))
# print(lst.index('A',4))
# lst.reverse()
# print(lst)


# #[예제.8]
# lst = [78,12,43,57,89]
# lst.sort(reverse=False) # 오름차순 
# print(lst)

# lst.sort(reverse=True) # 내림차순
# print(lst)


# num = 0
# numbers = [10, 20, 30, 40, 50, 60, 70]
# for n in numbers:
#     num += n
#     print(num)  # 누적 결과 출력
# print("결과값 {}입니다.".format(num))

#1~45 까지 임의의 값을 중복없이 6개 생성하여 출력하는 코드 작성
# import random
# for i in range(6):
#   print(random.randint(1,45))



# lst_sec = ['홍길동', '남', 36], ['김수양', '여', 32],['박담소', '남', 28]

# for person in lst_sec:
#   [0] == '홍길동'
#   print("이름", person[0])
#   print("이름", person[1])
#   print("이름", person[2])
#   print()



# [문제.4]
# - 기존 gugu List에 추가로 9개의 List를 생성 하여 곱셈 결과를 저장
# - [[1단],[2단],[3단],[4단],[5단],[6단],[7단],[8단],[9단]]
gugu = []
for x in range(1,10):  # x라는값은 1~9까지 변경되는 작업을 수행함.
  gugu.append([])      # 비어있는 리스트 속에 비어있는 리스트가 만들어짐.[[]]
  for y in range(1,10):   # y값도 1~9까지 바뀌면서 동작
    gugu[x-1].append(x*y) # gugu index번호를 지정하기 위해서 -1을 지정함. 1이라는 값을 가지고 

for x in range(1, 10):
  for y in range(1, 10):
    print('{} X {} = {}'.format(x, y, gugu[x-1][y-1]))

# 위에서 저장 한 List를 출력


