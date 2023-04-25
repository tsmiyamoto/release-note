def is_prime(n):
    if n < 0:
        print("n must be greater than 0")
        return False
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    print(is_prime(n))
