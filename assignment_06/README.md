# 과제#6 시간 복잡도 분석


- 코드를 분석하여 시간 복잡도 및 점근적 상한 함수(big-oh, $O$)를 구현하는 과제입니다. 
- 점근적 상한 함수는 **최악의 상황**을 고려한다는 것에 유의합니다.
- 모든 코드는 `complexity.py` 파일에 작성하며, 파일명을 변경하면 안 됩니다.
- 각 문제에 대한 `problem**()` 함수를 구현합니다.

- $f(n)$와 $g(n)$은 각각 시간 복잡도 함수 및 점근적 상한 함수입니다.
    
    - $f(n)$: 시간 복잡도 함수 (time complexity function)
    - $g(n)$: 점근적 상한 함수 (asymptotically upper bound function)

- $T_{i}$ 는 시간 비용을 나타내며, $T_{i}$ 를 합하여 $f(n)$을 정확하게 구현해야 합니다. 즉, $g(n)$은 다양한 정답이 존재할 수 있지만, $f(n)$은 정답이 정해져 있습니다.

- $c$와 $n_{0}$는 점근적 상한 함수를 정의할 때 임의로 정하는 상수이며, $c$와 $n_{0}$는 각각 실수 및 정수로서 0보다 크고 11보다 작습니다 ($1 ≤ c, n_{0} ≤ 10$).
- 테스트는 $c \cdot g(n)$이 $f(n)$의 **밀착 상한(tight upper bound)**인지 확인하기 위하여 $n$에 $n_{0}$보다 큰 수를 대입하여 $c \cdot g(n)$과 $f(n)$의 비율, $c \cdot g(n)/f(n)$을 검사하는 방식으로 이루어집니다. $c \cdot g(n)/f(n)$은 20보다 작아야 합니다.


$$\lim_{n\to\infty} \frac{c \cdot g(n)}{f(n)} \le 20 $$


- `problem**()` 함수는 분석한 코드에 대한 $f$, $g$, $c$, $n_{0}$를 반환합니다. 함수 $f$와 $g$를 `problem**()`의 내부에 정의합니다 (내재 함수, nested function).


- 제출 기한은 **2023년 5월 9일 오후 11시 59분** 입니다.
- `complexity.py`의 코드 템플릿은 아래와 같습니다.


```Python
def problem01():
    def f(n):
        return # n에 관한 수식
        
    def g(n):	
        return # n에 관한 수식
            
    c = 0
    n0 = 0

    return f, g, c, n0


def problem02():
    def f(n):
        return # n에 관한 수식
        
    def g(n):	
        return # n에 관한 수식
            
    c = 0
    n0 = 0

    return f, g, c, n0


def problem03():
    def f(n):
        return # n에 관한 수식
        
    def g(n):	
        return # n에 관한 수식
            
    c = 0
    n0 = 0

    return f, g, c, n0


def problem04():
    def f(n):
        return # n에 관한 수식
        
    def g(n):	
        return # n에 관한 수식
            
    c = 0
    n0 = 0

    return f, g, c, n0


def problem05():
    def f(n):
        return # n에 관한 수식
        
    def g(n):	
        return # n에 관한 수식
            
    c = 0
    n0 = 0

    return f, g, c, n0
```



 



## 문제(1)	`maximum` 함수의 시간 복잡도 분석 [20점]

- 아래 `maximum` 함수(`seq`의 길이는 `n`) 코드의 시간 복잡도를 분석하여 $f(n)$, $g(n)$, $c$, $n_{0}$를 반환하는 함수 `problem01`을 구현하시오.
 
```Python
def maximum(seq):
    maxval = -1                      # T1 = 1 
    for elem in seq:                 # T2 = 1
        if elem > maxval:            # T3 = 1
            maxval = elem            # T4 = 1
        # end of if
    # end of for
    return maxval                    # T5 = 1
```

- 아래 수식은 위 코드에 대한 점근적 상한 분석의 예시이다.

$$
\begin{align*}
f(n) &= T_{1} + (T_{2}  + T_{3} + T_{4})n + T_{5}  \\
     &= (T_{2} + T_{3} + T_{4})n + (T_{1} + T_{5})  \\
     &= 3n + 2 \\
     &\leq c \cdot n, \enspace \text{for}\enspace c = 4, n\geq n_{0} = 2. \\
g(n) &= n. \\
f(n) &\in O(g(n)).
\end{align*}
$$


## 문제(2)	`multiply_allpairs` 함수의 시간 복잡도 분석 [20점]

- 아래 `multiply_allpairs` 함수(seq의 길이는 `n`) 코드의 시간 복잡도를 분석하여 $f(n)$, $g(n)$, $c$, $n_{0}$를 반환하는 함수 `problem02`을 구현하시오.

```Python
def multiply_allpairs(seq):
    allpairs = []                    # T1 = 1
    for x in seq:                    # T2 = 1
        pairs = []                   # T3 = 1
        for y in seq:                # T4 = 1
            pairs.append(x*y)        # T5 = 1
        # end of for                 
        allpairs.append(pairs)       # T6 = 1
    # end of for
    return allpairs                  # T7 = 1
```


## 문제(3)	`multiply_square_matrices` 함수의 시간 복잡도 분석 [20점]

- 아래 multiply_square_matrices 함수(`a`, `b`는 `n`×`n` 행렬) 코드의 시간 복잡도를 분석하여 $f(n)$, $g(n)$, $c$, $n_{0}$를 반환하는 함수 `problem03`을 구현하시오.
 

```Python
def multiply_square_matrices(a, b):        
    n = len(a)                                     # T01 = 1
    c = []                                         # T02 = 1
    for i in range(n):                             # T03 = 1
        c.append([])                               # T04 = 1
        for j in range(n):                         # T05 = 1
            c[i].append(0.0)                       # T06 = 1
        # end of for
    # end of for

    for i in range(n):                             # T07 = 1
        for j in range(n):                         # T08 = 1
            for k in range(n):                     # T09 = 1
                 c[i][j] += (a[i][k] * b[k][j])    # T10 = 1
            # end of for
        # end of for
    # end of for
    return c                                       # T11 = 1
```


 ## 문제(4)	`DynamicArray.append` 함수의 시간 복잡도 분석 [20점]

- 아래 `DynamicArray.append` 함수(`self._length`가 `n`을 의미)의 시간 복잡도를 분석하여 $f(n)$, $g(n)$, $c$, $n_{0}$를 반환하는 함수 `problem04`를 구현하시오.
- 점근적 상한이 최악의 상황을 가정한다는 것에 유의하여 `resize`의 매개변수 `capacity`가 `n`에 따라 어떻게 변하는지 분석할 필요가 있다.

```Python
class DynamicArray:
    def __init__(self):        
        self._capacity = 1            
        self._length = 0
        self._arr = self._capacity * [None]
        
    def __str__(self):
        return str(self._arr)
        
    def __len__(self):
        return self._length 
    
    def __getitem__(self, i):
        return self._arr[i]
            
    def resize(self, capacity):        
        arr_new = capacity * [None]             # T1 = capacity
        for i in range(self._length):           # T2 = 1
            arr_new[i] = self._arr[i]           # T3 = 1
        # end of for

        self._arr = arr_new                     # T4 = 1
        self._capacity = capacity               # T5 = 1
    
    def append(self, elem):        
        if self._length == self._capacity:      # T6 = 1
            self.resize(2 * self._length)        
        self._arr[self._length] = elem          # T7 = 1
        self._length += 1                       # T8 = 1
        
    @property
    def capacity(self):
        return self._capacity

```



 ## 문제(5)	`repeat_duplication` 함수의 시간 복잡도 분석 [20점]

- 아래 `repeat_duplication` 함수 코드의 시간 복잡도를 분석하여 $f(n)$, $g(n)$, $c$, $n_{0}$를 반환하는 함수 `problem05`를 구현하시오.
-  `x0`는 정수형 매개변수로 가정한다.
 
```Python
def repeat_duplication(n, x0):
    x = [x0]                         # T1 = 1
    for i in range(n):               # T2 = 1
        y = []                       # T3 = 1
        for elem in x:               # T4 = 1
            y.append(elem)           # T5 = 1
            y.append(elem + 1)       # T6 = 1
        # end of for
        x = y                        # T7 = 1
    # end of for
    return x                         # T8 = 1
```
