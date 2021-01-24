## SWEA D02 1984번 문제

### < 1984. 중간 평균값 구하기 >

```python
T = int(input())

for test_case in range(1, T + 1):
  num_list = list(map(int, input().split())) # <== 짚고 넘어갈 부분
  
  max_num = max(num_list)
  min_num = min(num_list)
  
  avg = reound((sum(num_list) - max_num - min_num) / (len(num_list) - 2))
  print('#{} {}'.format(test_case, avg))
```

1984번 문제에서 `input().split()`으로 작성하면, 런타임 에러 없이 해당 문제를 패스할 수 있다.

**하지만 `input().split(' ')`으로 작성하면 런타임 에러가 발생한다. 이유는 다음과 같다.**

- `input().split()`으로 작성시 공백이 1개 이상이면 모두 공백으로 처리한다. -> 이 경우를 **코드1**로 칭하겠다.
- `input().split(' ')`으로 코드 작성시 only 공백 1개만을 기준으로 `split()`을 실행시킨다.  -> 이 경우를 **코드2**로 칭하겠다.
- 아무래도 테스트 케이스에 공백이 2개 이상(`'  '`)으로 된 부분이 존재하는 것 같다.
- **코드1**과 **코드2**를 모두 실험해본 결과 **코드1**의 경우만 해당 문제를 pass 할 수 있었다...!

#### 함수 `str.split(sep=None, maxsplit=-1)`

[python3.8 공식문서](https://docs.python.org/3.8/library/stdtypes.html)에 따르면 아래와 같다.

> If *sep* is not specified or is `None`, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a `None` separator returns `[]`.

여기서 내가 주목해야 하는 부분은 **runs of consecutive whitespace are regarded as a single separator** 이다. 대충 해석하면, 연속적인 스페이스는 하나로 본다는 의미이다. 

따라서, `sep=None`과 `sep=' '`는 확연히 다르다... (SWEA 댓글을 통해 문제점이 무엇인지 인식할 수 있었고, 여러 실험과 공식문서를 통해 에러의 발생 근거를 찾았다... ㅜ)

