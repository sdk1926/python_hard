# 파이썬 클래스 메소드 , 인스턴스 메소드, 스테틱 매소드 

# 기본 인스턴스 메소드 

class exo_member(object):
    '''
    Idol_member
    Author : sdk
    Date : 210705
    '''

    #class 변수 
    korea_album_count = 21

    def __init__(self, realname, nickname, age, ability, solo_album=0):
        self._realname = realname
        self._nickname = nickname
        self._age = age 
        self._ability = ability
        self._solo_album = solo_album 

    # instance method 
    def names(self):
        return f'{self._realname} : {self._nickname}'

    def detail_info(self):
        return f'Member Detail Info : {self._realname} {self._nickname} {self._age} 능력 : {self._ability} 솔로앨범 개수: {self._solo_album}'

    def get_solo_album_count(self):
        return f'{self._nickname}의 솔로앨범 개수 : {self._solo_album}'
    
    def get_all_album_count(self):
        return f'{self._nickname}의 솔로앨범 개수 + 그룹 엘범 개수 : {self._solo_album + exo_member.korea_album_count}'

    def __str__(self):
        return f'{self.detail_info()}'

    # class Method 
    @classmethod
    def raise_album_count(cls, count):
        if count < 1:
            print('1 이상을 추가해주세요.')
            return
        cls.korea_album_count += count
        print('앨범 개수 추가가 반영됐습니다.')

    # Class method
    @classmethod
    def add_member(cls, realname, nickname, age, ability, solo_album=0):
        return cls(realname, nickname, age, ability, solo_album)

    # static Method
    @staticmethod
    def is_solo(inst):
        if inst._solo_album > 0:
            return f'{inst._nickname}은 솔로앨범을 {inst._solo_album}장 발매 했습니다.'
        return f'{inst._nickname}은 솔로앨범을 발매하지 않았습니다.'


member1 = exo_member('김민석', '시우민',32, '결빙')
member2 = exo_member('김준면', '수호', 31, '물', 1)
member3 = exo_member('변백현','백현', 30, '빛', 4)

# 기본 정보 
print(member1)
print(member2)
print(member3)

# 전체 정보 
print(member1.detail_info())
print(member2.detail_info())
print(member3.detail_info())

# 솔로 앨범 정보 
print(member1.get_solo_album_count())
print(member2.get_solo_album_count())
print(member3.get_solo_album_count())

# 2020년 기준 앨범 개수 
print(member1.get_all_album_count())
print(member2.get_all_album_count())
print(member3.get_all_album_count())

# 2021년 앨범 추가 
exo_member.raise_album_count(1)

print()
# 2021년 기준 앨범 개수 
print(member1.get_all_album_count())
print(member2.get_all_album_count())
print(member3.get_all_album_count())

# 클래스 메소드를 활용해서 멤버 추가 
member4 = exo_member.add_member('도경수', '디오', 30, '힘')
member5 = exo_member.add_member('김종인', '카이', 28, '순간이동', 1)
print(member4.get_all_album_count())
print(member5.get_all_album_count())

# 솔로앨범 유무(스테틱 메소드 미사용)
def is_solo(inst):
    if inst._solo_album > 0:
        return f'{inst._nickname}은 솔로앨범을 {inst._solo_album}장 발매 했습니다.'
    return f'{inst._nickname}은 솔로앨범을 발매하지 않았습니다.'

print(is_solo(member1))
print(is_solo(member2))
print(is_solo(member3))
print(is_solo(member4))
print()
# 솔로앨범 유무(스테틱 메소드 사용)
print(exo_member.is_solo(member1))
print(exo_member.is_solo(member2))
print(exo_member.is_solo(member3))
print(exo_member.is_solo(member4))
print()
# 인스턴스로 접근 
print(member1.is_solo(member1))
print(member2.is_solo(member2))
print(member3.is_solo(member3))
print(member4.is_solo(member4))