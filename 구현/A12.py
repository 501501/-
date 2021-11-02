# 벽면의 크기 n
# 작업 순서 build_frame [x, y, a, b]
# x, y: 교차점의 좌표    a: 구조물의 종류 (0: 기둥, 1: 보)     b: 구조물 설치/삭제 (0: 삭제, 1: 설치)
# answer: 가로가 3인 2차원 배열 [x, y, a] 형식

# 가능한 구조물인지 체크
def possible(answer):
    for x, y, stuff in answer:
        # 기둥인 경우
        if stuff == 0:
            # 바닥 or 보의 한쪽 끝부분 위 or 또 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False

        # 보인 경우
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame

        # 삭제하는 경우
        if operate == 0:
            answer.remove([x, y, stuff])
            # 가능한 구조물인지 확인
            if not possible(answer):
                answer.append([x, y, stuff])
        # 설치하는 경우
        if operate == 1:
            answer.append([x, y, stuff])
            # 가능한 구조물인지 확인
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)