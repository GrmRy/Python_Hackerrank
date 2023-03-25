if __name__ == '__main__':
    N = int(input())
    temp = []
        
    for _ in range(N):
        cmd, *values = input().split() 
        values = tuple(map(int, values))
        if cmd == 'print':
            print(temp)
        else:
            eval(f"temp.{cmd}{values}")
