#   za 1 bod:
#   t<9,n<5, m<9


saved = {}


def A_rec(x, t, n):

    if n == 0:
        return t + 1
    if n == 1:
        return x + t
    if n == 2:
        return x * t
    if n == 3:
        return x ** t
    if t == 0:
        return 1

    print("ASSERT", t, n)
    assert False


def ae(t, n, m, steps=False):
    for nn in range(n + 1):
        for tt in range(t + 1):
            # print("Adding n=", nn, "t=", tt)

            if 0 <= nn <= 3:
                saved[(nn, tt)] = A_rec(3, tt, nn) % 2 ** m

            elif (nn, tt - 1) in saved:
                new_y = saved[(nn, tt - 1)]
                saved[(nn, tt)] = A_rec(3, new_y, nn - 1) % 2 ** m

            else:
                saved[(nn, tt)] = A_rec(3, tt, nn) % 2 ** m
            if steps:
                print("A(n=", nn, "t=", tt, ") =", saved[(nn, tt)])

    y = saved[(n, t - 1)]
    return A_rec(3, y, n - 1) % 2 ** m


def main():
    print(ae(t=7, n=4, m=8,steps=True))


if __name__ == '__main__':
    main()

