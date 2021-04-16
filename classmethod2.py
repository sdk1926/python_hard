# 클래스 메소드, 인스턴스 메소드, 스태틱 메소드 

# 기본 인스턴스 매소드 

class Student(object):
    '''
    Student class
    Author : sdk
    Date : 2021.04.13
    Description : Class, Static, Instance Method
    '''
    
    # Class 변수
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email , grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email 
        self._grade = grade
        self._tuition = tuition 
        self._gpa =gpa

    # Instance Method
    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    # Instance Method 
    def detail_info(self):
        return 'Student Detail Info: {},{},{},{},{},{}'.format(self._id,self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method 
    def get_fee(self):
        return 'Before Tuition -> Id : {}. fee : {}'.format(self._id, self._tuition)
    
    # Instance Method
    def get_fee_culc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # Instance Method
    def __str__(self):
        return 'Student Info -> name : {} grade : {} email : {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.tuition_per = per 
        print('Succed! tuition increased!')
        # cls는 Student클래스와 같다. 

    # Class Method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method 
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient.'

    

# 학생 인스턴스 
student_1 = Student(1, 'kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student2@naver.com', '2', 500, 4.3)

print(student_1)
print(student_2)
print()

# 전체 정보 
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보(인상전)
print(student_1.get_fee())
print(student_2.get_fee())

print()

# 학비 인상 (클래스 메소드 미사용)
# Student.tuition_per = 1.2

# 학비 인상 (클래스 메소드 사용)
Student.raise_fee(1.3)

# 학비 정보(인상후)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
print()

# 클래스 메소드 인스턴스 생성 실습 
student_3 = Student.student_const(3, 'Park', 'Minji', 'student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(3, 'Cho', 'Sunghan', 'student4@gmail.com', '4', 600, 4.1)

# 전체 정보 
print(student_3.detail_info())
print(student_4.detail_info())

# 학생 학비 변경 확인 
print(student_3._tuition)
print(student_4._tuition)
print()

# 장학금 혜택 여부(스테틱 메소드 미사용)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient.'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))
print()
# 장학금 혜택 여부(스테틱 메소드 사용)
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4)) 
print()
print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))
# 클래스에 바로 접근해도 되고 인스턴스에 접근해도 된다. (스태틱 메소드는)


print(student_1.is_scholarship_st(student_2))