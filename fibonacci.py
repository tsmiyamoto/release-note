# calc fibonacci series up to n
def fib(n):
    if n < 0:
        print("n must be greater than 0")
        return

    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        # a, b = b, a+b
        t = b
        b = a + b
        a = t
    print()


if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
