import time


def add_200_1(n):
    for i in range(2):
        n += 100
    return n


def add_200_2(n):
    for i in range(100):
        n += 2
    return n


def print_100(n):
    for i in range(100):
        print(n)
    return n


def sum_n(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


def sum_suq(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += i + j
    return sum


def fun3(n):
    while n > 2:
        print("divide")
        n /= 2
    return n


print(add_200_1(10))

start_time1 = time.time()
print(add_200_2(100000))
end_time1 = time.time()

start_time2 = time.time()
print_100(100000)
end_time2 = time.time()

print(end_time1 - start_time1)
print(end_time2 - start_time2)

n = [[1, 2], [3, 4]]

print([row[1] for row in n])
