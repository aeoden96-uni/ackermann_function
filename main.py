#   za 1 bod:
#   t<9,n<5, m<9
from collections import deque


def ack_i(m, n):

    stack = deque([])
    stack.extend([m, n])

    while len(stack) > 1:
        n, m = stack.pop(), stack.pop()

        if   m == 0:
            stack.append(n + 1)
        elif n == 0:
            stack.extend([m-1, 1])
        else:
            stack.extend([m-1, m, n-1])

    return stack[0]


saved = {}


def A_rec(x, t, n):
    print("Current:",t,",",n)
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

    if (n, t) in saved:
        print("succes",(n, t))
        new_t = saved[(n, t)]
    else:

        print("No", (n, t), "A(", x, ",", t - 1, ",", n, ")")
        saved[(n, t)] = A_rec(x, t - 1, n)
        new_t = saved[(n, t)]
        print("Added add")
    print(saved)
    new_rez = A_rec(x, new_t, n - 1)

    return new_rez


def ae(t, n, m):

    for nn in range(n + 1):
        for tt in range(t + 1):
            print("Adding", (nn, tt))
            saved[(nn, tt)] = A_rec(3, tt, nn)

    return A_rec(3, t, n) % 2 ** m


def main():
    print(ae(t=7, n=4, m=8))
    # print(saved)


if __name__ == '__main__':
    main()

    print("end")
