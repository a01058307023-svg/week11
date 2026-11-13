# bug3_logic.py
#
# 문제: 학생 점수 리스트에서 가장 큰 점수와 통과 인원 수를 계산하는 함수다.
# 아래 두 함수의 로직 오류를 수정한다.
#
# 함수 설명
#   find_max(scores)              -> 리스트에서 가장 큰 값을 반환
#   count_pass(scores, cutoff=60) -> cutoff 이상인 점수의 개수를 반환
#
# 예시
#   data = [70, 85, 60, 95]
#   find_max(data) -> 95
#   count_pass(data) -> 4
#
# 주의사항
#   - 통과 기준은 60점 이상이다.
#   - 점수는 0 이상 정수로 가정한다.
# ---------------------------------------------------------------------------


def find_max(scores):
    if not scores:
        raise ValueError("scores must not be empty")

    biggest = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > biggest:
            biggest = scores[i]
    return biggest


def count_pass(scores, cutoff=60):
    count = 0
    for score in scores:
        if score >= cutoff:
            count += 1
    return count


if __name__ == "__main__":
    data = [70, 85, 60, 95]
    print("최대값:", find_max(data))
    print("합격 수:", count_pass(data))