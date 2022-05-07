import sys

#카멜케이스 : 단어를 대소문자로 구분하여 작명
camelCase: int = 1

#스네이크 케이스 : 각 단어를 언더스코어(_)로 구분
snake_case: int = 1

#타입 힌트 : 파이썬은 동적 타이핑 언어지만 타입을 지정할 수 있는 타입 힌트 추가
a: str = "1"
b: int =1

#타입 힌트를 써서 함수의 파라미터 및 리턴 값을 명시적으로 선언
def fn(a: int) -> bool:
    pass

c: str = 1 #문자열에 정수를 할당하는 방식은 지양

#리스트컴프리헨션
#가독성은 좋은 편이지만 표현식 2개를 넘지 않도록 한다. 복잡하면 가독성 떨어짐
d = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
original = {'test' : 1, 'test2' : 2} 
e = {key : value for key, value in original.items()}

#제너레이터
#루프의 반복 동작을 제어할 수 있는 루틴의 형태
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

g = get_natural_number()
print(next(g))
for _ in range(0,10):
    print(next(g))

def generator():
    yield 1
    yield 'string'
    yield True

g2 = generator()
print(g2)
print(next(g2))
print(next(g2))
print(next(g2))

# Range
# 제너레이터의 방식을 활용하는 대표적인 함수

a = [n for n in range(100)]
b = range(100)

# len(a) == len(b) -> True 길이는 동일
# 생성조건만 보관하기에 메모리 점유율은 동일
print(sys.getsizeof(a))
print(sys.getsizeof(b))

#enumerate
#enumerate()는 열거하다의 뜻의 함수로, 여러 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴

a = [1,2,3,4,5]
print(list(enumerate(a)))

#print
print('A1', 'B2')

print('aa', end=' ')
print('bb')
a = ['A', 'B']
print(''.join(a))

idx = 1
fruit = 'Apple'
print('{0}:{1}'.format(idx+1, fruit))
print('{}:{}'.format(idx+1, fruit))

print(f'{idx+1}:{fruit}')

#locals
#로컬 심볼 테이블 딕셔너리를 가져오는 메소드, 로컬에 선언된 모든 변수를 조회 가능
import pprint
print(pprint.pprint(locals()))