# class 선언 

class VectorP(object):
    
    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return(i for i in (self.__x,self.__y)) # Generator 

    @property
    def x(self):
        return self.__x 

    @x.setter
    def x(self, v):
        print('Called Property X Setter')
        self.__x = v 

    @property
    def y(self):
        return self.__y 

    @y.setter
    def y(self, v):
        print('Called Property X Setter')
        self.__y = v 

# 객체 선언 
v = VectorP(20,40)

# print('EX1-1 -', v.__x, v.__y)

# Getter, Setter
print('EX1-2 -', dir(v), v.__dict__)
print('EX1-3 -', v.x, v.y)

# Iter 확인   
for val in v:
    print('EX1-2 -', val)

# __slot__
# 파이썬 인터프리터에게 통보 
# 해당 클래스가 가지는 속성을 제한 
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용 공간 대폭 감소 
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 set 형태를 사용 

class TestA(object):
    __slots__ = ('a',)

class TestB(object):
    pass 

use_slot = TestA()
no_slot = TestB()

print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__)
print('EX2-3 -', no_slot)
print('EX2-4 -', no_slot.__dict__)

# 메모리 사용량 비교 
import timeit 

# 측정을 위한 함수 선언 
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner

print(min(timeit.repeat(repeat_outer(use_slot), number=1000000)))
print(min(timeit.repeat(repeat_outer(no_slot), number=1000000)))

# 객체 슬라이싱 

class Objects:

    def __init__(self):
        self._numbers = [ n for n in range(1, 10000, 3)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]

s = Objects()
print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s))
print('EX3-3 -', len(s._numbers))
print('EX3-4 -', s[1:100])
print('EX3-5 -', s[-1])
print('EX3-6 -', s[::10])

print()
print()

# 파이썬 추상클래스 
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것 
# 자체적으로 객체 생성 불가 
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야 함 


