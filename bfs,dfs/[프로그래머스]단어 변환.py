from collections import deque

tmp = "abcdefghijklmnopqrstuvwxyz"
alpha = list(tmp)


def solution(begin, target, words):
    answer = 0
    answer = bfs(begin, 0, target, words)

    return answer


def bfs(start, depth, target, words):
    q = deque()
    visited = []
    q.append((start, depth))
    visited.append(start)

    while q:
        word, depth = q.popleft()
        if word == target:
            return depth

        for i in range(len(word)):
            for char in alpha:
                new_word = word[0:i] + char + word[i + 1:len(word)]
                if new_word in words and new_word not in visited:
                    visited.append(new_word)
                    q.append((new_word, depth + 1))
    return 0