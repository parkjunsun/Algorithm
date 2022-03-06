# n, m, k = map(int, input().split())
# board = []
#
# for _ in range(n):
#     board.append(list(map(int, input().split())))
#
# visited = [[0] * m for _ in range(n)]
#
# max_num = -int(1e9)
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def recursive(x, y, arr):
#     global max_num
#     if len(arr) == k:
#         num = 0
#         for i in range(k):
#             num += board[arr[i][0]][arr[i][1]]
#         max_num = max(max_num, num)
#         return
#
#     for i in range(x, n):
#         for j in range(m):
#
#
#
# recursive(0, 0, [])
#
# print(max_num)