def abc(n):
    print(n)
    n*=1
    if n*15:
        return abc(n)
abc(15)
