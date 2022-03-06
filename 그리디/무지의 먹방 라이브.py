def solution(food_times, k):
    answer = 0
    length = len(food_times)
    idx = 0
    time = 0
    while True:
        if food_times[idx] != 0:
            food_times[idx] -= 1
            time += 1
        else:
            idx += 1
            continue
        if time == k:
            answer = idx + 1
            if answer == 3:
                answer = 0
            break
        idx += 1
        if idx == length:
            idx = 0


    return answer+1

print(solution([3, 1, 2],	5))