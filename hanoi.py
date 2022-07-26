def hanoi(n, start, support, finish):
    if (n == 1):
        print("Move " + start + " to " + finish)
    else:
        hanoi(n-1, start, finish, support)
        print("Move " + start + " to " + finish)
        hanoi(n-1, support, start, finish)

if __name__ == '__main__':
    hanoi(3, 'L', 'C', 'R')