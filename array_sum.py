import time


def main():
    array_length = int(input("Length of array? (eg. 10 -> [1, 2, 3,...,10]): "))

    arr = [(x + 1) for x in range(array_length)]

    start = time.time()
    sum_iteration = array_sum(arr)
    end = time.time()

    print("\nIterative Output: {0}\nTime Elapsed: {1:.4f}ms\n".format(sum_iteration, ((end - start) * 1000)))

    try:
        start = time.time()
        sum_recursion = array_sum_rec(arr, len(arr))
        end = time.time()

        print("Recursive Output: {0}\nTime Elapsed: {1:.4f}ms\n".format(sum_recursion, ((end - start) * 1000)))
    except RecursionError:
        print("Maximum recursion depth exceeded\n")


def array_sum(array):
    s = 0
    for i in array:
        s += i
    return s


def array_sum_rec(array, index):
    if index <= 0:
        return 0
    return array_sum_rec(array, index - 1) + array[index - 1]


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            exit()
