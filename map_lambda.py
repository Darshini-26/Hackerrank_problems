cube = lambda x:x*x*x
def fibonacci(n):
    a = []

    for i in range(n):
        a.append(i) if i < 2 else a.append(a[i - 2] + a[i - 1])

    return a
