
# 과제#4 작업내역 관리 구현

- 스택(stack)을 이용하여 “실행 취소(Undo)” 및 “다시 실행(Redo)”이 가능한 작업내역 관리 기능  (history)을 구현하는 과제입니다.
- 파이썬 프로그래밍 언어로 작업내역 관리 기능 클래스 `History`를 구현해 봅시다.
- 스택의 동작 방식을 이해하기 위해 [VisuAlgo](https://visualgo.net/en)를 참고할 수 있습니다.
- 모든 코드는 `history.py` 파일에 작성하며, 파일명을 변경하면 안 됩니다 (대소문자도 변경하면 안 됩니다).
- `test_with_assert.py` 파일을 이용하여 일부 경우에 대해 테스트 할 수 있습니다. 필요한 경우 `test_with_assert.py`에 테스트 코드를 추가하시길 바랍니다.
- 제출 기한은 **2024년 4월 30일 오후 11시 59분** 입니다.
- `History` 클래스의 템플릿은 아래와 같습니다.

```Python
class History(object):
    def __init__(self):
        pass
    
    def __str__(self):
        pass

    @property
    def current_state(self):
        pass

    def append(self, state):
        pass

    def undo(self):
        pass
    
    def redo(self):
        pass
    
    def clear(self):
        pass
```

## 문제(1) `History` 클래스 및 멤버변수 작성 [10점]

`History` 클래스는 다음과 같이 인스턴스 멤버변수(member variable)를 갖는다.

- `_stack_undo`: Undo 스택 객체. 새로운 상태가 추가되거나 Redo를 실행하는 경우 Undo 스택에 상태 객체가 차곡차곡 쌓이게 된다.

- `_stack_redo`: Redo 스택 객체. Undo를 실행하면 Undo 스택에 있던 상태 객체들이 나오는 순서대로 Redo 스택으로 옮겨 쌓는다.

- `History` 클래스의 `__init__`에서 각 멤버변수의 객체 인스턴스를 생성한다.
- `_stack_undo`: 리스트(list) 객체로 초기화한다.
- `_stack_redo`: 리스트(list) 객체로 초기화한다.


## 문제(2) `current_state` 프로퍼티(property) 정의 [10점]
- `current_state`는 현재 상태(state)를 반환하는 프로퍼티이다.

- “현재 상태”는 일련의 작업들이 수행된 이후 “현재 프로그램 상태”나 “현재 작업 공간의 상태”를 의미한다.

- 파이썬의 모든 객체가 상태(state)를 나타내는 객체가 될 수 있으며, 테스트에서는 간단하게 문자열을 이용하여 상태를 나타낼 수 있다.

- “현재 상태”는 Undo 스택에 마지막으로 추가된 상태이다. 즉, `@property`를 이용하여 Undo 스택의 최상단 객체를 반환하도록 구현한다 (스택의 “peek” 참고).

- Undo 스택이 비어 있는 경우 None을 반환한다.

- 현재 상태는 외부에서 변경되면 안 되기 때문에 `@current_state.setter`는 정의하지 않는다.


## 문제(3) `append(state)` 멤버함수 구현 [20점]
- 새로운 상태 객체를 추가하는 함수이다.

- Undo 스택에 상태 객체를 추가한다.

- 새로운 상태가 Undo 스택에 추가되면 Redo 스택에 있는 모든 상태는 제거한다 (파이썬 `list`의 `clear` 참고).


## 문제(4) `undo()` 멤버함수 구현 [20점]
- Undo 스택의 최상단 상태 객체를 꺼낸 후 (스택의 “pop” 참고 ), 현재 상태를 바로 이전의 상태로 갱신하는 함수이다.

- 즉, `undo()` 함수를 호출하면 Undo 스택에서 상태 객체를 꺼낸 다음 Redo 스택에 추가한다.

- Undo 스택의 최상단에 있는 상태 객체가 현재 상태를 의미하기 때문에 Undo 스택에서 객체를 꺼내는 것만으로 현재 상태를 갱신하는 기능을 구현할 수 있다.

- Undo 스택이 비어 있는 경우 아무것도 하지 않는다.

- `append` 함수가 정상적으로 동작해야 채점이 된다.

## 문제(5) `redo()` 멤버함수 구현 [20점]

- Redo 스택의 최상단 상태 객체를 꺼낸 후 (스택의 “pop” 참고), 현재 상태를 변경하는 함수이다.

- 즉, `redo()` 함수를 호출하면 Redo 스택에서 상태 객체를 꺼낸 다음 Undo 스택에 추가한다.

- Undo 스택의 최상단에 있는 상태 객체가 현재 상태를 의미하기 때문에 Redo 스택에서 꺼낸 객체를 다시 Undo 스택에 추가하는 것만으로 현재 상태를 갱신하는 기능을 구현할 수 있다.

- Redo 스택이 비어 있는 경우 아무것도 하지 않는다.

- `append` 함수가 정상적으로 동작해야 채점이 된다.

## 문제(6)  `clear()` 멤버함수 구현 [20점]

- Undo 및 Redo 스택을 모두 비운다.

- `append` 함수가 정상적으로 동작해야 채점이 된다.

