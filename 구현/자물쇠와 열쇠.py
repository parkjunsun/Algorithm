def solution(key, lock):
    answer = True
    M = len(key)
    N = len(lock)
    key = [key]     #key배열에 90도씩 회전한 key집어넣을것임, 원본key미리 넣어놓음

    def init():
        res = [[0] * M for _ in range(M)]
        return res

    def padding(lock):          #lock 주변으로 padding 시킬 함수
        T = N + 2 * (M - 1)     #최소로 padding 할 크기
        res = [[0] * T for _ in range(T)]   #padding 일단 0으로 채워놓음
        for i in range(N):
            for j in range(N):
                res[i + M - 1][j + M - 1] = lock[i][j]      #padding 안에 원래 lock 위치에 맞게 값 넣어줌
        return res

    def check(key):     #window sliding을 하면서 모두 1 인지 체크할 것임
        from copy import deepcopy
        T = len(lock_padding)
        M = len(key)
        for gap1 in range(T - M + 1):       #key가 padding에서 아래로 sliding 할 수 있는 최대 거리
            for gap2 in range(T - M + 1):   #key가 padding에서 오른쪽으로 sliding 할 수 있는 최대거리
                breaker = False
                cand_padding = deepcopy(lock_padding)   #key가 이동할 padding이 필요함
                for i in range(M):
                    for j in range(M):
                        cand_padding[i + gap1][j + gap2] += key[i][j]       #key값을 padding에 대입해봄
                check_area = []     #lock 부분 추출용
                for i in range(M-1, M-1+N): # M-1에서 시작하는 이유는 lock[0][0]은 cand_padding입장에서는 cand_padding[M-1][M-1]이다 머릿속에 그림을 계속 생각하자, M-1+N은 시작점에서 자물쇠 크기만큼 더해준것
                    temp = []
                    for j in range(M-1, M-1+N):
                        temp.append(cand_padding[i][j])
                    check_area.append(temp)

                for i in range(len(check_area)):
                    for j in range(len(check_area[0])):
                        if check_area[i][j] != 1:
                            breaker = True
                            break
                    if breaker:
                        break
                if not breaker:
                    return True
        return False

    for _ in range(3):
        new_key = init()
        for i in range(M):
            for j in range(M):
                new_key[j][M - 1 - i] = key[-1][i][j]   #90도 회전 (p,q) --> (q,M-1-p) 정사각2차원에서 이런규칙,  직사각형일때는 직접해봐야할듯
        key.append(new_key)

    lock_padding = padding(lock)

    for i in range(4):      #90도 돌린거 한번씩 다 확인
        answer = False
        candidate_key = key[i]
        if check(candidate_key):
            return True
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))