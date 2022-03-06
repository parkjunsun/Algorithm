def solution(N, stages):
    total = len(stages)
    arr = []
    for i in range(1, N+1):
        son = stages.count(i)
        if son == 0:
            arr.append((0, i))
        else:
            arr.append((son / total, i))
        total -= son
    arr.sort(key=lambda x:(-x[0], x[1]))
    return arr



