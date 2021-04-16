# 클래스 상세 설명 
# 클래스 변수, 인스턴스 변수 

class Student():
    """
    Student Class
    Author: sdk
    Date: 2021.04.12 
    """

    # 클래스 변수 
    student_count = 0 

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수 
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email
        # 클래스 변수에 접근하기 
        Student.student_count += 1 

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('student Detail Info : {} {} {}'.format(self._name, self._email, self._details))        

    def __del__(self):
        Student.student_count -= 1 

# self의 의미
studt1 = Student('cho', 2 ,3, {'gender': 'Male', 'score1': 65, 'score2': 44})
studt2 = Student('chang', 4 ,1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'stu2@naver.com')

# 아이디 값이 다르다. 
print(id(studt1))
print(id(studt2))

# is 는 아이디 값을 비교, == 는 값을 비교 
print(studt1._name == studt2._name)
print(studt1 is studt2)

# dir & __dict__ 확인
print(dir(studt1)) 
print(dir(studt2)) 
print(studt1.__dict__)
print(studt2.__dict__)

# Doctring - 주석을 출력 
print(Student.__doc__) 
print()

# 실행 
studt1.detail_info()
studt2.detail_info()

# 에러 
# Student.detail_info()

# 에러 방지 
Student.detail_info(studt1)
Student.detail_info(studt2)

# 비교 
print(studt1.__class__, studt2.__class__)
print(id(studt1.__class__) == id(studt2.__class__))

print()

# 인스턴스 변수 
# 직접 접근(PEP 문법적으로 권장x)

# studt1._name = 'HAHAHA'
print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

print()
print()

# 클래스 변수 

# 접근 
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)

print()
print()

# 공유 확인 
print(Student.__dict__)
print()
print(studt1.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색 
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

del studt2
print(studt1.student_count)
print(Student.student_count)

