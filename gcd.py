# 最大公約数を求める関数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    import sys

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(gcd(a, b))
