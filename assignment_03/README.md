# 과제#3 배열 함수 구현

- 가장 기본적인 자료구조인 배열에 대해 간단한 연산 및 작업을 수행하는 함수들을 구현해 보는 실습입니다.
- 제출 기한은 **2024년 4월 23일 오후 11시 59분** 입니다.
- 각 문제의 요구사항에 따라 파이썬 프로그래밍 언어로 함수를 구현해 봅시다.
- 모든 함수는 `array_utils.py` 파일에 작성하며, 파일명을 변경하면 안 됩니다 (대소문자도 변경하면 안 됩니다).
- `array_utils.py`의 템플릿은 아래와 같습니다.


    ```Python
    import os.path as osp


    # 문제(1)
    def get_max(arr):
        # 코드 작성...
        return 0


    def get_min(arr):
        # 코드 작성...
        return 0


    def get_sum(arr):
        # 코드 작성...
        return 0


    def get_mean(arr):
        # 코드 작성...
        return 0


    def get_median(arr):
        # 코드 작성...
        return 0


    # 문제(2)
    def count_files(paths):
        """
        paths: 디렉토리 및 파일 경로들이 포함되어 있는 list 객체.
        """
        n_files = 0
        # 코드 작성...
        return n_files


    def filter_fname(fpaths, word):
        """
        fpaths: 파일 경로들이 포함되어 있는 list 객체.
        word: 파일 이름에 포함되어야 하는 단어.
        """
        fpaths_filtered = []
        # 코드 작성...
        return fpaths_filtered


    def filter_ext(fpaths, ext):
        """
        fpaths: 파일 경로들이 포함되어 있는 list 객체.
        ext: 파일확장자 (예: "jpg", "png")
        """
        fpaths_filtered = []
        # 코드 작성...
        return fpaths_filtered


    def change_fname(fpaths, old_word, new_word):
        """
        fpaths: 파일 경로들이 포함되어 있는 list 객체.
        old_word: 파일 이름에서 교체 대상이 되는 단어.
        new_word: 파일 이름에 새롭게 추가할 단어.
        """
        fpaths_new = []
        # 코드 작성...
        return fpaths_new


    def change_dpath(fpaths, dpath):
        """
        fpaths: 파일 경로들이 포함되어 있는 list 객체.
        dpath: 새로운 디렉토리 경로.    
        """
        fpaths_new = []
        # 코드 작성...
        return fpaths_new
    ```


## 문제(1) 통계 함수 구현하기
- 통계와 관련된 기본적인 함수를 구현해 봅시다.
- 본 문제에서 코드를 작성할 때 일부 내장 함수(`max`, `min`, `sum`), 표준 라이브러리(standard library), 외부 라이브러리(3rd-party library)의 기능은 사용할 수 없습니다.
- 본 문제에서 `arr`은 `int`형 자료형이 담긴 `list`로 주어집니다. `arr`은 원소를 최대 $1000$개까지 가질 수 있으며, 각 원소는 $-1000$ 이상 $-1000$ 이하의 값을 가집니다.
- 각 수식에서 $a$는 배열을 나타내며, $a[i]$는 인덱스 $i$에 해당하는 원소를 의미합니다.
- 각 수식에서 $n$은 배열의 길이, 즉 배열 원소의 개수를 의미합니다.

### (a) `get_max(arr)` 구현하기 [10점]
- 작업
    - 배열 `arr`의 원소 중 가장 큰 값을 찾아 반환하는 함수를 구현.
- 반환값의 자료형
    - `int`

### (b) `get_min(arr)` 구현하기 [10점]
- 작업
    - 배열 `arr`의 원소 중 가장 작은 값을 찾아 반환하는 함수를 구현.
- 반환값의 자료형
    - `int`

### (c) `get_sum(arr)` 구현하기 [10점]
- 작업
    - 배열 `arr`의 원소의 값을 모두 합하는 함수를 구현.
    - 배열 $a$의 원소의 합 $S$는 다음과 같은 수식으로 나타낼 수 있음.

$$ S = \sum_{i=0}^{n-1}{a[i]} $$

- 반환값의 자료형
    - `int`

### (d) `get_mean(arr)` 구현하기 [10점]
- 작업
    - 배열 `arr`의 원소의 값을 모두 합하는 함수를 구현.
    - 배열 $a$의 원소의 평균 $a_{mean}$은 다음과 같은 수식으로 나타낼 수 있음.

$$ a_{mean} = \frac{1}{n}\sum_{i=0}^{n-1}{a[i]} $$

- 반환값의 자료형
    - `float`
    - 단, 결과값이 정수인 경우 `int`도 허용

### (e) `get_median(arr)` 구현하기 [10점]
- 작업
    - 배열 `arr`에서 중간값을 구하는 함수를 구현.
    - `arr`은 오름차순으로 정렬되었다고 가정 (테스트에서 정렬된 배열이 들어옴).
    - 중간값은 다음과 같이 구할 수 있음.
    
        - n이 홀수: $median = arr\Big[\frac{n}{2}\Big]$
    
        - n이 짝수: $median = \frac{1}{2}\Bigg(arr\Big[\frac{n}{2}-1\Big] + arr\Big[\frac{n}{2}\Big]\Bigg)$
    
    - 여기서 주의해야 될 점은, $\frac{n}{2}$이 인덱스로 사용할 수 있는 정수를 의미한다는 것 (파이썬에서 `n // 2`로 구할 수 있음).

- 반환값의 자료형
    - `float`
    - 단, 결과값이 정수인 경우 `int`도 허용

## 문제(2) 파일 및 디렉토리 경로 관리 함수 구현하기
- 파일 및 디렉토리 경로(path)를 다루는 기본적인 함수를 구현해 봅시다.

- 본 문제에서 코드를 작성할 때 표준 라이브러리(standard library) 및 외부 라이브러리(3rd-party library)의 기능은 사용할 수 없습니다.

- 단, `os.path.splitext`, `os.path.join`, `os.path.basename`, `os.path.dirname`, `os.path.normpath` 함수는 사용할 수 있습니다.

- `paths`에는 디렉토리 경로 및 파일 경로가 모두 포함되어 있습니다. 디렉토리 경로는 확장자를 가지지 않는다고 가정합니다. (확장자의 예: `jpg`, `png`, `dat`).

- 본 문제에서 `paths`은 `str`형 자료형이 담긴 `list`로 주어집니다. `paths`은 경로를 최대 $1000$개까지 가질 수 있으며, 각 경로의 길이는 최대 $1000$ 입니다.

- `fpaths`에는 파일 경로만 포함되어 있습니다.

- 본 문제에서 `fpaths`은 `str`형 자료형이 담긴 `list`로 주어집니다. `fpaths`은 경로를 최대 $1000$개까지 가질 수 있으며, 각 경로의 길이는 최대 $1000$ 입니다.

- 각종 디렉토리 이름이 포함되어 있는 **파일 경로**와 **파일 이름**을 구분해야 합니다.

- 디렉토리 경로의 예시: `jpg`나 `png`와 같이 확장자가 없으면 디렉토리 경로로 취급합니다.
    ```Python
    "/data/images/cau-photos-2023-03/"
    "/data/images/cau-photos-2023-03/photos-2023-0301"  
    ```

- 파일 경로의 예시: `jpg`나 `png`와 같이 확장자가 있으면 파일 경로로 취급합니다.
    ```Python
    "/data/images/cau-photos-2023-03/image-017.jpg"
    "/data/images/cau-photos-2023-03/photo-017.png"
    "/data/images/cau-photos-2023-03/meta-017-jpg.dat"
    ```

- 다음은 `os.path.splitext`, `os.path.join`, `os.path.basename`, `os.path.dirname`, `os.path.normpath` 함수 사용 예시입니다.

    ```Python
    import os.path as osp

    # 다음과 같이 파일 경로와 확장자를 분리하고 싶을 때 splitext() 함수를 사용
    fpath = "/data/images/cau-photos-2023-03/photo.jpg" 
    dpath_fname, ext = osp.splitext(fpath)
    print(dpath_fname)  # /data/images/cau-photos-2023-03/photo
    print(ext)  # .jpg

    # 디렉토리나 파일 이름 등을 결합하고 싶을 때 join() 함수를 사용.
    # 굳이 join() 함수를 사용하는 이유는 운영체제마다 경로 구분자(separator)가 다르기 때문.
    fpath = osp.join("/data/images/cau-photos-2023-03", "photo.jpg")
    print(fpath)  # /data/images/cau-photos-2023-03\photo.jpg

    # 구분자를 통일 시키고 싶은 경우 normpath() 함수를 사용.
    fpath = osp.join("/data\\images", "cau-photos-2023-03", "photo.jpg")
    print(fpath)  # 구분자가 엉망진창: /data\images\cau-photos-2023-03\photo.jpg

    fpath_new = osp.path.normpath(fpath)
    print(fpath)  # Windows 11 기준: \data\images\cau-photos-2023-03\photo.jpg

    # 경로에서 최말단 이름만 얻고 싶은 경우 basename()을 사용.
    fpath = "/data/images/cau-photos-2023-03/photo.jpg" 
    fname = osp.basename(fpath)
    print(fname)  # photo.png

    fpath = "/data/images/cau-photos-2023-03" 
    dname = osp.basename(fpath)
    print(dname)  # cau-photos-2023-03

    # 경로에서 최말단 이름을 제외한 경로를 얻고 싶은 경우 dirname()을 사용.
    # 즉, 파일 이름을 제외한 디렉토리 경로를 얻고 싶을 때 사용 가능.
    fpath = "/data/images/cau-photos-2023-03/photo.jpg" 
    dpath = osp.dirname(fpath)
    print(dpath)  # /data/images/cau-photos-2023-03

    dpath = "/data/images/cau-photos-2023-03" 
    dpath_parent = osp.dirname(dpath)
    print(dpath_parent)  # /data/images
    ```


### (a) `count_files(paths)` 구현하기 [10점]
- 작업
    - 배열 `paths`에서 파일 경로의 개수를 반환하는 함수를 구현.
    - 확장자가 없는 경로는 디렉토리 경로로 취급함.
- 반환값의 자료형
    - `int`

### (b) `filter_fname(fpaths, word)` 구현하기 [10점]
- 매개변수 자료형
    - `word` : 길이가 최대 $1000$인 `str`
- 작업
    - 배열 `fpaths`에 포함된 파일 경로 중 파일 이름에 `word`가 포함된 파일 경로만 추려서 `list` 객체로 반환.
- 반환값의 자료형
    - `str` 자료형 원소가 담긴 `list`

### (c) `filter_ext(fpaths, ext)` 구현하기 [10점]
- 매개변수 자료형
    - `ext` : 길이가 최대 $3인 `str`
- 작업
    - 배열 `fpaths`에 포함된 파일 경로 중 파일 확장자가 `ext`인 파일 경로만 추려서 `list` 객체로 반환.
- 반환값의 자료형
    - `str` 자료형 원소가 담긴 `list`

### (d) `change_fname(fpaths, old_word, new_word)` 구현하기 [10점]
- 매개변수 자료형
    - `old_word` : 길이가 최대 $1000$인 `str`
    - `new_word` : 길이가 최대 $1000$인 `str`
- 작업
    - 배열 `fpaths`에 포함된 파일 경로에서, 파일 이름에 포함된 `old_word` 단어를 `new_word`로 교체한 파일 경로를 새로운 `list` 객체로 반환.
    - `str` 객체의 `replace`를 활용하면 일부 문자열을 쉽게 교체할 수 있음.
- 반환값의 자료형
    - `str` 자료형 원소가 담긴 `list`

### (e) `change_dpath(fpaths, dpath)` 구현하기 [10점]
- 매개변수 자료형
    - `dpath` : 길이가 최대 $1000$인 `str`
- 작업
    - 배열 `fpaths`에 명시된 파일들을 새로운 디렉토리 경로 `dpath`로 옮기거나 복사하기 위해 디렉토리 경로를 변경하는 함수임.
    - 배열 `fpaths`에 포함된 파일 경로에서, 디렉토리 경로와 파일 이름을 구분한 후 새로운 디렉토리 경로와 파일 이름을 결합하여 새로운 파일 경로를 생성.
    - 새로운 파일 경로들은 새로운 `list` 객체로 반환.
- 반환값의 자료형
    - `str` 자료형 원소가 담긴 `list`
