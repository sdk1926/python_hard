# 파이썬 심화
# 데이터 모델(data model)
# Nametuple 실습 
# 파이썬의 중요한 핵심 프레임 워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화 
## 모든 객체 -> id, type -> value 
# 파이썬 -> 일관성 
 
# 일반적인 튜플 사용  
# x값과 y값이 뭔지 알려줘야한다. 
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt # 루트 함수 뺴옴
line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
print('EX1-1 - ', line_leng1)



# 네임드 튜플 사용

from collections import namedtuple

# 네임드 튜플 선언 
Point = namedtuple('Point', 'x y')

# 두 점 선언 
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# 계산 
line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# 출력 
print('EX1-2 -', line_leng2)
print('EX1-3 -', line_leng2 == line_leng1)

# 네임드 튜플 선언 방법 
Point1 = namedtuple('Point', ['x','y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')  # 공백이 생기면 다른 인자로 간주한다. 
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = false

# 출력 
print('EX2-1 -', Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}  # dict형태로 키값을 정할 수 있음 

# 객체 생성 

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40) # rename=True 값이 알아서 겹치지 않는 이름으로 바꿔준다. 
p5 = Point3(**temp_dict) # dict 형태를 키로 쓸려면 앞에 ** 을 붙여야함 

# 출력 
print('EX2-2 -', p1, p2, p3, p4, p5)

print()
print()

# 사용 
print('EX3-1 -', p1[0]+p2[1]) # index error 주의
print('EX3-2 -', p1.x+p2.y)  # 클래스 변수 접근 방식

# Unpacking 
x,y = p3

print('EX3-3 -', x+y)

# Rename 테스트 
print('EX3-4 -', p4)

# 네임드 튜플 메소드 

temp = [52,38] 

# _make() : 새로운 객체 생성 
p4 = Point1._make(temp)

print('EX4-1 -', p4)

# _fields: 필드 네임 확인 
print('EX4-2 -', p1._fields,p2._fields,p3._fields,p4._fields,p5._fields)

# _asdict() : Dict 반환

print('EX4-3 -', p1._asdict(),p2._asdict())

# _replqce() : 수정 된 '새로운' 객체 반환 

print('EX4-4 -', p2._replace(y=100))
print(p2)  
print()
print()

# 실 사용 실습 
# 학생 전체 그룹 생성 
# 반 20명, 4개의 반 -> (A,B,C,D) 번호 

# 네임드 튜플 선언 
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언 
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()
print(ranks,numbers)

# LIst comprehension 
students = [Classes(rank,number) for rank in ranks for number in numbers]

print('EX5-1 -',len(students))
print('EX5-2 -',students)
print(students[4].rank)

# 가독성이 안 좋은 경우 
students2 = [Classes(rank,number) for rank in 'A B C D'.split() for number in [str(n) for n in range(1,21)]]
print(students2)

print('EX6-1 -',len(students2))
print('EX6-2 -',students2)

# 출력 
for s in students:
    print('EX7-1 - ', s)