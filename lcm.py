from gcd import gcd


# 最大公約数を求める関数
def lcm(x, y):
    return (x * y) // gcd(x, y)


if __name__ == "__main__":
    import sys

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(lcm(a, b))
