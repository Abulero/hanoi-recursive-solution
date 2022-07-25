def hanoi(n, start, support, finish):
    if (n > 1):
        hanoi(n-1, start, finish, support)
        move(start, finish)
        hanoi(n-1, support, start, finish)
    else:
        move(start, finish)

def move(origin, destination):
    print(origin + " -> " + destination)

if __name__ == '__main__':
    hanoi(3, 'Left', 'Center', 'Right')