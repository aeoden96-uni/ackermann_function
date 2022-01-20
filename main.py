#   za 1 bod:
#   t<9,n<5, m<9
import time


saved = {}


def A_rec(t, n, m):
    x = 3
    if n == 0:
        return t + 1 % 2 ** m
    if n == 1:
        return x + t % 2 ** m
    if n == 2:
        return x * t % 2 ** m
    if n == 3:
        return x ** t % 2 ** m
    if t == 0:
        return 1

    return A_rec(A_rec(t - 1, n, m) % 2 ** m, n - 1, m) % 2 ** m


def A_iter(t, n, m):
    x = 3
    if n == 0:
        return t + 1 % 2 ** m
    if n == 1:
        return x + t % 2 ** m
    if n == 2:
        return x * t % 2 ** m
    if n == 3:
        return x ** t % 2 ** m
    if t == 0:
        return 1

    if (t - 1, n) in saved:
        # print("     alry has ", (t - 1, n))
        new_y = saved[(t - 1, n)]
    else:
        new_y = A_iter(t - 1, n, m) % 2 ** m
        # print("     added ", (t - 1, n))
        saved[(t - 1, n)] = new_y

    # if (new_y, n - 1) in saved:
    #     var =
    var = A_iter(new_y, n - 1, m) % 2 ** m
    saved[(new_y, n - 1)] = var
    return var

    # print("ASSERT", t, n)
    # k = 0
    # for (i, j) in saved:
    #     if j > k:
    #         print()
    #         k += 1
    #     print((i, j), "=", saved[(i, j)], "    ", end="")
    #
    # assert False


def ae_iter(t, n, m, steps=False):
    for nn in range(n + 1):
        for tt in range(t + 1):

            # print("Adding n=", nn, "t=", tt)

            if 0 <= nn <= 3:
                saved[(tt, nn)] = A_iter(tt, nn, m) % 2 ** m

            elif (tt - 1, nn) in saved:

                new_y = saved[(tt - 1, nn)]

                saved[(tt, nn)] = A_iter(new_y, nn - 1, m) % 2 ** m

            else:
                saved[(tt, nn)] = A_iter(tt, nn, m) % 2 ** m
            if steps:
                print("A( 3,",tt,",", nn, ") =", saved[(tt, nn)] )

    y = saved[(t - 1, n)]
    return A_iter(y, n - 1, m) % 2 ** m


def ae(t, n, m, steps=True, recursive=False, measure_time=False):
    if measure_time:
        start_time = time.time()

    value = A_rec(t, n, m) if recursive else ae_iter(t, n, m, steps=steps)

    if measure_time:
        print("### %s seconds ###" % (time.time() - start_time))

    return value




def main():

    print(ae(t=8, n=8, m=8, steps=False, recursive=False, measure_time=True))

    # print(A_rec(t=12, n=9, m=8))
    # 2875
    # 59
    # 59
    # 315


if __name__ == '__main__':
    main()
