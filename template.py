"""
[문제 정보]
- 플랫폼: 프로그래머스
- 난이도: Lv.
- 제목: 
- 핵심 알고리즘/자료구조: 
- 시간 복잡도 목표: O()

[설계 접근]
1. 
2. 
"""

def solution(param1, param2):
    answer = 0
    # TODO: 풀이 로직 작성
    return answer


if __name__ == "__main__":
    # (입력값1, 입력값2, ..., 기댓값)
    test_cases = [
        (["sample_input1"], "sample_input2", "expected_output"),
    ]

    for i, (*inputs, expected) in enumerate(test_cases, 1):
        result = solution(*inputs)
        status = "PASS" if result == expected else f"FAIL (기댓값: {expected}, 결과: {result})"
        print(f"Test {i}: {status}")
