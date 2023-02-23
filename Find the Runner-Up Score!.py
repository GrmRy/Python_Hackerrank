if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    urut=sorted(arr)
    besar=max(urut)
    while besar in urut:
        urut.remove(besar)
    print(max(urut))
