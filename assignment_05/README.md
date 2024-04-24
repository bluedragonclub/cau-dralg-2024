# 과제#5 단일연결리스트 구현

- 단일연결리스트 클래스를 Python 프로그래밍 언어로 구현하는 과제입니다.
- 단일연결리스트의 개념도 중요하지만, 이번 실습을 통해 프로그래밍 실력을 향상시켜 봅시다.
- 단일연결리스트의 구현을 이해하기 위해 [VisuAlgo](https://visualgo.net/en)를 참고할 수 있습니다.
- 모든 코드는 `singlylinkedlist.py` 파일에 작성하며, 파일명을 변경하면 안 됩니다.
- 특정 멤버함수들의 경우 다른 멤버함수가 완벽하게 구현되어야 테스트가 가능합니다.
- 제출 기한은 **2023년 4월 25일 오후 11시 59분** 입니다.
- 코드 템플릿은 아래와 같습니다.


```Python
class Node(object):
    
    def __init__(self, data=None):
        pass
    

class SinglyLinkedList(object):
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass

    def __len__(self):
        pass 
            
    def empty(self):
        pass
        
    def insert(self, i, data):
        pass

    def remove(self, i):
        pass
              
    def clear(self):
        pass
    
    def get(self, i):
        pass
    
    def pop(self, i=None):
        pass
    
    def search(self, target, start=0):
        pass

    def extend(self, sll):
        pass 
```


## 문제(1)	`Node` 클래스 작성 [5점]
- `Node` 클래스는 `_data` 및 `_next`를 멤버변수(member variable)로 갖는다. `_data` 및 `_next` 멤버변수의 값은 파이썬 프로퍼티(property)를 통해 읽어오고 변경할 수 있어야 한다.
- `Node` 클래스의 `__init__`에서 `_data` 및 `_next` 멤버변수를 생성한다.
- `@property`를 통해 각 멤버변수의 값을 읽어올 수 있도록 구현한다.
- `@<프로퍼티이름>.setter`를 통해 각 멤버변수의 값을 변경할 수 있도록 구현한다.

## 문제(2)	`SinglyLinkedList` 클래스 작성 [5점] 
- `SinglyLinkedList` 클래스는 `_head`, `_tail` 및 `_num_nodes`를 멤버변수로 갖는다. `SinglyLinkedList`의 멤버변수는 객체 내부에서만 사용하므로 프로퍼티를 정의할 필요는 없다.
- `SinglyLinkedList` 클래스의 `__init__`에서 `_head`, `_tail` 및 `_num_nodes` 멤버변수를 추가한다.

## 문제(3)	`SinglyLinkedList` 클래스의 `__len__` 멤버함수 구현 [5점]
- 단일연결리스트에 존재하는 노드의 개수를 반환한다.
- `_num_nodes`를 이용하여 구현한다.

## 문제(4)	`SinglyLinkedList` 클래스의 `empty()` 멤버함수 구현 [5점]
- 노드가 전혀 없는 경우 `True`를 반환하고 그렇지 않은 경우 `False`를 반환한다.
- `_num_nodes`를 이용하여 구현한다.

## 문제(5)	`SinglyLinkedList` 클래스의 `insert(i, data)` 멤버함수 구현 [10점]
- 인덱스(index) `i`로 지정한 위치에 `data`로 지정한 객체를 추가하는 멤버함수이다.
- `data`는 파이썬에 있는 모든 객체를 참조할 수 있어야 한다.
- 인덱스 `i`는 i+1번째 `Node` 객체를 의미한다.
- 허용되지 않는 인덱스 `i`에 대해 예외(exception)를 발생시켜야 한다. 인덱스 `i`가 0보다 작거나 연결리스트의 길이(i.e., `_num_nodes`) 보다 큰 경우, `IndexError` 예외를 발생시킨다.
- 인덱스 `i`로 지정한 위치에 `Node` 객체가 이미 존재한다면 해당 객체는 뒤로 보내고 삽입하고자 하는 새로운 `Node` 객체를 인덱스 `i` 위치에 오도록 삽입한다.

## 문제(6)	`SinglyLinkedList` 클래스의 `pop(i)` 멤버함수 구현 [10점]
- 인덱스(index) `i`로 지정한 위치에 있는 `Node` 객체를 연결리스트에서 삭제한 후, 삭제된 `Node` 객체의 `data`를 반환(return)하는 멤버함수이다.
- 상황에 따라 `_head`, `_tail`, `_num_nodes`를 적절하게 갱신해야 한다.
- 사용자가 인덱스 `i`를 지정하지 않은 경우 연결리스트의 가장 마지막 `Node`의 `data`를 반환하도록 한다. 즉, 인덱스 `i`의 기본값(default)을 `None`으로 설정하고, `pop` 멤버함수가 호출되었을 때 인덱스가 지정되지 않았다면 (즉, 인덱스 `i`의 값이 `None`이면) 연결리스트의 마지막 `Node`의 `data`를 반환하도록 한다.
- 연결리스트가 비어 있는 상황에서 `pop()` 멤버함수를 호출한 경우, `IndexError` 예외를 발생시킨다.
- 인덱스의 의미 및 예외처리는 `insert` 멤버함수 부분을 참고한다. 단, 인덱스의 범위는 `0`부터 `_num_nodes - 1`이다.
- 참고로 파이썬 `list` 객체의 `pop`과 동일한 기능을 수행한다고 볼 수 있다.

## 문제(7)	`SinglyLinkedList` 클래스의 `remove(i)` 멤버함수 구현 [15점]
- 인덱스(index) `i`로 지정한 위치에 있는 `Node` 객체를 삭제하는 멤버함수이다.
- 인덱스 `i`로 지정한 위치에 있는 노드 객체를 제거하고, 그 이전 노드와 그 이후 노드를 연결해 주면 된다. 
- `pop()`과 달리 삭제한 노드의 데이터는 반환하지 않는다.
- `pop()`을 이용하거나 `pop()`의 코드를 토대로 작성하면 좋다.
- 인덱스의 의미 및 예외처리는 `pop` 멤버함수 부분을 참고한다. 
- 연결리스트가 비어 있는 상황에서 `remove()` 멤버함수를 호출한 경우, 예외를 발생시키지 말고, 객체가 아무것도 하지 않도록 작성한다.

## 문제(8) `SinglyLinkedList` 클래스의 `clear()` 멤버함수 구현 [10점]
- `SinglyLinkedList` 내에 있는 모든 `Node` 객체를 제거하는 함수이다.
- `Node` 객체를 참조하는 변수가 하나도 없도록 코드를 작성한다. 즉, 가비지 콜렉션(garbage collection)에 따라 `Node` 객체가 자동으로 삭제될 수 있도록 한다.
- 연결리스트를 순회(traverse)하면서 각 `Node` 객체의 `next`에 `None`을 대입한다.
- `SinglyLinkedList`의 `_head`와 `_tail`을 `None`으로 설정하고, `_num_nodes`에 0을 대입한다.

## 문제(9)	SinglyLinkedList 클래스의 `get(i)` 멤버함수 구현 [10점]
- 인덱스(index) `i`로 지정한 위치에 있는 `Node` 객체의 `data`를 반환(return)하는 멤버함수이다.
- 연결리스트가 비어 있는 상황에서 `get()` 멤버함수를 호출한 경우, `IndexError` 예외를 발생시킨다.
- 인덱스의 의미 및 예외처리는 `pop` 멤버함수 부분을 참고한다.

## 문제(10)	`SinglyLinkedList` 클래스의 `search(target, start)` 멤버함수 구현 [10점]
- `target`으로 지정한 객체와 동일한 `data`를 갖는 `Node` 객체를 찾아, `data` 객체 및 인덱스 `i`를 반환한다 (즉, `return data, i`).
- 연결리스트에서 `target`을 찾지 못한 경우 `None`과 `-1`을 반환한다 (즉, `return None, -1`).
- `start`는 탐색을 시작하는 인덱스이며 기본값은 0이다. 즉, `start` 인덱스에 해당되는 위치부터 탐색하기 시작한다.
- `target`의 값이 `None`이 될 수도 있다.
- `start`에 대해 인덱스 예외처리를 적용한다. 인덱스의 의미 및 예외처리는 `pop` 멤버함수 부분을 참고한다.
- `SinglyLinkedList` 객체의 길이가 0인 상황에서 `search()` 멤버함수를 호출한 경우, `pop` 멤버함수처럼 예외를 발생시킨다.

## 문제(11)	`SinglyLinkedList` 클래스의 `extend(sll)` 멤버함수 구현 [15점]
- 다른 연결리스트의 모든 데이터를 기존 연결리스트의 마지막에 차례로 추가하는 멤버함수이다.
- 전달인자로 들어온 `sll` 연결리스트의 각 데이터에 대해 새로운 `Node` 객체를 생성하여 기존 연결리스트의 말단에 차례로 추가한다.
- 새로운 `Node` 객체를 추가한 후 기존 연결리스트의 `_num_nodes` 멤버변수를 갱신하는 것을 잊지 않는다.
- 전달인자 `sll`은 `SinglyLinkedList` 객체만 받아들일 수 있도록 한다. 따라서 사용자가 `sll`을 여타 객체로 설정한 경우 `TypeError` 예외를 발생시키도록 한다.
