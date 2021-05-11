# Decorator& closure 
# 파이썬 변수 범위(global)

def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(5)

b = 10 

def func_v2(a):
    print(a)
    print(b)

func_v2(5)

def func_v3(a):
    print(a)
    print(b)
    b = 5
###
# func_v3(5)

from dis import dis 
print(dis(func_v3))

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언 된 연결을 가지고 참조하는 방식 
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다. 

a = 10
print('EX2-1 -', a + 10)
print('EX2-2 -', a + 100)

# 결과를 누적 할 수 없을까? 
print('EX2-3 -', sum(range(1,51)))
print('EX2-4 -', sum(range(51,101)))

print()
print()

# 클래스 이용 
class Averager():
    def __init__(self):
        self._series = []
    
    def __call__(self,v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성 
avg_cls = Averager()

# 누적확인 
print(avg_cls(10))
print(avg_cls(20))
print(avg_cls(30))

# 클로저(Closure) 사용 
# 전역변수 사용 감소 
# 디자인 패턴 적용 

def closure_avg1():
    # Free variable
    series = []
    # 클로저 영역 
    def averager(v):
        # series = [] # check
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager  # 함수를 호출만 한다. 

avg_closure1 = closure_avg1()

print('EX4-1 -', avg_closure1(15))
print('EX4-2 -', avg_closure1(35))
print('EX4-3 -', avg_closure1(40))



