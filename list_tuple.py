# 시퀀스형 
# 컨테이너(Container) : 서로 다른 자료형[list, tuple, collections.deque]
# Flat : 한 개의 자료형 [str, bttes, bytearray, array.array, memoryview]
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str bytes 

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists 

chars = '!@#$%^&*()_+'
codes1 = []
for s in chars: 
    codes1.append(ord(s))

# Comprehending Lists 
codes2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세 
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x : x >40, map(ord, chars)))

print('EX1-1 -', codes1)
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)
print('EX1-5 -', codes3)
print('EX1-6 -', [chr(s) for s in codes1])
print('EX1-7 -', [chr(s) for s in codes2])
print('EX1-8 -', [chr(s) for s in codes3])
print('EX1-9 -', [chr(s) for s in codes4])

# Generator 

import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 x)
tuple_g = (ord(s) for s in chars)

# Array 
array_g = array.array('I', (ord(s) for s in chars))

print('EX2-1 -', tuple_g)
print('EX2-2 -', next(tuple_g))
print('EX2-3 -', next(tuple_g))
print('EX2-4 -', array_g)
print('EX2-5 -', array_g.tolist())

print()
print()

# 제네레이터 예제 
print('EX3-1 -', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print('EX3-2 -', s)

print()
print()

# 리스트 주의 할 점 
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3 

print('EX4-1 -', marks1)
print('EX4-1 -', marks2)

print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 -', marks1)
print('EX4-4 -', marks2)

# 증명 
print('EX4-5 -', [id(i) for i in marks1])
print('EX4-6 -', [id(i) for i in marks2])


import array
import resource

startMem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

mylist = []
for i in range(1,100000):
    mylist.append(i)

listMem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

myarray = array.array('i')
for i in range(1,100000):
    myarray.append(i)

arrayMem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

print("list를 만드는 데는 :", listMem-startMem)
print("array를 만드는 데는 : ", arrayMem-listMem)

# Tuple advanced 

# packing& Unpacking 

print('EX5-1 -', divmod(100,9))
print('EX5-2 -', divmod(*(100, 9)))
print('EX5-3 -', *(divmod(100, 9)))

x,y, *rest = range(10)
print('EX5-4 -', x,y,rest)
x,y, *rest = range(2)
print('EX5-5 -', x,y,rest)
x,y, *rest = 1, 2, 3, 4, 5
print('EX5-6 -', x,y,rest)

# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print('EX6-1 -', l, m ,id(l), id(m)) 

l = l * 2  # 연산가능
m = m * 2

print('EX6-2 -', l, m, id(l), id(m))  

l *= 2 
m *= 2

print('EX6-3 -', l, m, id(l), id(m))  # 튜플만 메모리 주소가 바뀌었다. 

# sort vs sorted 
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 '새로운' 객체 반환 

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))  # 역순정렬
print('EX7-3 -', sorted(f_list, key=len)) # 길이 순으로 정렬 
print('EX7-4 -', sorted(f_list, key=lambda x:x[-1]))  # 끝 글자 순으로 정렬 
print('EX7-5 -', sorted(f_list, key=lambda x:x[-1], reverse=True)) # 끝 글자 역순으로 정렬 
print('EX7-6 -', sorted(f_list)) # 원본 안변경됨

# sort : 정렬 후 객체 직접 변경
# 반환 값 확인 None

a = f_list.sort()
# 원본이 변경되기 때문에 원본을 출력해야 값이 나옴 
print('EX-7 -', f_list.sort(), f_list)
print('EX-8 -', f_list.sort(reverse=True), f_list)
print('EX-9 -', f_list.sort(key=len), f_list)
print('EX-10 -', f_list.sort(key=lambda x:x[-1]), f_list)
print('EX-11 -', f_list.sort(key=lambda x:x[-1], reverse=True), f_list)
