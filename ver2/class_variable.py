# 파이썬 클래스 변수

class Idol_member(object):
    """
    Idol_member class
    Aythor : sdk 
    Date : 210705
    """
    # 클래스 변수 
    member_count = 0

    def __init__(self, name, group, gender, age, agency, song=None):
        # 인스턴스 변수 
        self._name = name
        self._group = group
        self._gender = gender 
        self._age = age
        self._agency = agency 
        self._song = song

        Idol_member.member_count +=1

    def __str__(self):
        return f'str: {self._name}'

    def __repr__(self):
        return f'repr : {self._group}'

    def detail_info(self):
        print(f'Current Id: {id(self)}')
        print(f'Member Detail Info : {self._name} {self._group} {self._gender}')

    def __del__(self):
        Idol_member.member_count -= 1

# self의 의미 
member1 = Idol_member('카이', '엑소', 'male', 28, 'SM엔터테인먼트')
member2 = Idol_member('슬기', '레드벨벳', 'female', 28, 'SM엔터테인먼트', 'psycho')

# dir & __dict__ 확인 
print(dir(member1))
print(member1.__dict__)

# Doctring
print(member1.__doc__)

# 실행 
member1.detail_info()
member2.detail_info()

# 에러 
# Idol_member.detail_info() self가 없잖아!! 

Idol_member.detail_info(member1)
Idol_member.detail_info(member2)

# 비교 
print(member1.__class__)
print(member2.__class__)

# 인스턴스 변수 
# 직접 접근 (권장x)
member2._name = '슬기2'
print(member2._name, member2._group)
print(member1._name, member1._group)

print()

# 클래스 변수 
print(member1.member_count)
print(member2.member_count)
print(Idol_member.member_count)

# 공유 확인 
print(Idol_member.__dict__)
print(member1.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색 
# 즉 동일한 이름으로 변수 생성 가능