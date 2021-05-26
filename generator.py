# Python Generator 
## 파이썬 반복형 종류 
## iter, next 함수 
## Generator 장점 
## Generator 코딩 실습 
## Generator 내장 함수 실습 

# 파이썬 반복형 종류 
# for, collections, text file, List, Dict, Set, Tuple, Unpacking, *args
# 공부할 것 : 반복형 객체 내부적으로 iter 함수 내용, 제네레이터 동작 원리, yield from 

# 반복 간으한 이유? -> iter(x) 함수 호출 

t = 'ABCDEF'

# for 사용 
for c in t:
    print('EX1-1 -', c)

# while 사용 
w = iter(t)

while True:
    try:
        print('EX1-2 -', next(w))
    except StopIteration:
        break 

from collections import abc 

# 반복형 확인 
print('EX1-3 -', hasattr(t, '__iter__'))
print('EX1-4 -', isinstance(t, abc.Iterable))

# next 사용 
