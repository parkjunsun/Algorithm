x, y, w, h = map(int, input().split())

if x > w // 2 and y > h // 2:
    print(min(w-x, h-y))
elif x <= w // 2 and y > h // 2:
    print(min(x, h-y))
elif x <= w //2 and y <= h // 2:
    print(min(x, y))
elif x > w // 2 and y <= h // 2:
    print(min(w-x, y))