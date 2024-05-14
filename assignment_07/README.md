# 과제#7 정렬 함수 사용


- Python에서 기본적으로 제공하는 정렬 함수를 사용해 보는 과제입니다. 참고로 Python에서 제공하는 기본 정렬 알고리즘은 [Timsort](https://ko.wikipedia.org/wiki/%ED%8C%80%EC%86%8C%ED%8A%B8)입니다.
- Python에서 제공하는 `list.sort()` 및 `sorted()` 함수를 활용하여 구현합니다.
- Python **공식 문서**를 참고하여 `list.sort()` 및 `sorted()`의 매개변수를 적절히 설정하여 구현합니다.
- `sort_dict_by_key` 및 `sort_dict_by_val` 함수의 경우 `dict.items()` 함수를 활용할 수 있습니다.
- 모든 코드는 `sort.py` 파일에 작성하며, 파일명을 변경하면 안 됩니다.
- 제출 기한은 **2024년 5월 28일 오후 11시 59분** 입니다.
- `sort.py`의 코드 템플릿은 아래와 같습니다.


```Python
from typing import List, Tuple

def sort_list(seq, inplace=True, ascending=True) -> List[object]:
    pass

def sort_objects(seq, key, inplace=True, ascending=True) -> List[object]:
    pass

def sort_dict_by_key(kv, ascending=True) -> List[Tuple[object, object]]:
    pass

def sort_dict_by_val(kv, ascending=True) -> List[Tuple[object, object]]:
    pass
```

 
## 문제(1) `list`에 포함된 객체를 원소의 크기로 정렬하는 `sort_list(seq, inplace=True, ascending=True)` 함수를 구현하시오 [25점]
- 전달인자 `seq`는 "sequence"를 의미하며, `list` 타입이다.
- `inplace`가 `True`인 경우, 새로운 `list`를 생성하지 않고 전달인자로 주어진 원본 `list`를 정렬한 후 반환한다. 즉, 정렬 이후 매개변수 `seq`를 반환한다.
- `inplace`가 `False`인 경우, 원본 `list`에 대한 복사본을 생성하여 정렬한 후 반환한다. 매개변수 `seq`를 반환해서는 안 된다.
- 원본 `list`를 복사할 때는 얕은 복사(shallow copy)를 이용한다 (즉, `seq[:]`로 복사).
- `ascending`이 `True`인 경우 오름차순으로 정렬하며, `False`인 경우 내림차순으로 정렬한다.

## 문제(2) `list`에 포함된 객체들을 정렬하는 `sort_objects(seq, key, inplace=True, ascending=True)` 함수를 구현하시오 [25점]
- 전달인자 `seq`는 "sequence"를 의미하며, `list` 타입이다.
- `seq`의 원소는 Python의 모든 객체가 될 수 있으며, `key`로 설정한 조건 또는 항목으로 대소 비교가 가능해야 한다.
- `inplace`와 `ascending`의 동작방식은 문제(1)과 동일하다.
- `sort_objects` 구현 후 다음 예시 코드로 테스트하기 위해서는 "...생략..."으로 표기한 부분에 전달인자를 적절히 설정해야 한다.

```Python
class Student(object):
    
    def __init__(self, student_id, gender, age):
        self.student_id = student_id
        self.gender = gender
        self.age = age
        
    def __str__(self):
        return "Student(%d, %s, %d)"%(self.student_id, self.gender, self.age)
        
    def __repr__(self):
        return str(self)
        
students = [
    Student(20221234, "M", 22),
    Student(20215678, "F", 21),
    Student(20231004, "M", 20),
    Student(20201234, "F", 23),
    Student(20191234, "M", 25),
]
        

print()
students_sorted = sort_objects(students, ...생략...)
for st in students_sorted:
    print(st)
    
# Student(20191234, M, 25)
# Student(20201234, F, 23)
# Student(20215678, F, 21)
# Student(20221234, M, 22)
# Student(20231004, M, 20)
    
print()
students_sorted = sort_objects(students, ...생략...)
for st in students_sorted:
    print(st)

# Student(20231004, M, 20)
# Student(20215678, F, 21)
# Student(20221234, M, 22)
# Student(20201234, F, 23)
# Student(20191234, M, 25)

print()
students_sorted = sort_objects(students, ...생략...)
for st in students_sorted:
    print(st)
    
# Student(20215678, F, 21)
# Student(20201234, F, 23)
# Student(20231004, M, 20)
# Student(20221234, M, 22)
# Student(20191234, M, 25)
```



## 문제(3) dict를 키(key)로 정렬하는 `sort_dict_by_key(kv, ascending=True)` 함수를 구현하시오 [25점]
- 전달인자 `kv`는 `dict`이며, `kv`의 키(key)와 값(value)의 튜플을 키에 따라 정렬하여 `list`로 반환한다.
- 즉, 키에 따라 정렬된 `list`, `[(key_1, val_1), (key_2, val_2), …, (key_n, val_n)]`을 반환한다. 예를 들어, 오름차순인 경우 $key_{1} ≤ key_{2} ≤ \cdots ≤ key_{n}$ 조건을 만족해야 한다.
- `ascending`이 `True`인 경우 오름차순으로 정렬하며, `False`인 경우 내림차순으로 정렬한다.

## 문제(4) `dict`를 값(value)으로 정렬하는 `sort_dict_by_val(kv, ascending=True)` 함수를 구현하시오 [25점]
- 전달인자 `kv`는 `dict`이며, `kv`의 키(key)와 값(value)의 튜플을 값에 따라 정렬하여 `list`로 반환한다.
- 즉, 값에 따라 정렬된 `list`, `[(key_1, val_1), (key_2, val_2), …, (key_n, val_n)]`을 반환한다. 예를 들어, 오름차순인 경우 $val_{1} ≤ val_{2} ≤ \cdots ≤ val_{n}$ 조건을 만족해야 한다.
- `ascending`이 `True`인 경우 오름차순으로 정렬하며, `False`인 경우 내림차순으로 정렬한다.

