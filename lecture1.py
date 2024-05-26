# this is my first program

print(f"Hello World, my name is Nuri")  # this is the print command

x = 5
y = 2.5
z = "I am Z"
a = []
b = True
c = 5 + 9j
d = [5, 2.5, True, "Hello"]

print(f"This is the value of x: {x}")
print(d)

#e = int(input("Please enter the value of e:"))
#print(e)

print(6 + 8)
print(9 - 5)
print(9 + 2 * 3)
print(2 ** 2 ** 3)  #256
print(2 ** 3 ** 2)  #512
print(4 & 7)
print(a and b and c)  # HW

x = 75
if x > 15:
    print(f"{x} is greater than 15")
elif x == 15:
    print(f"{x} is equal to 15")
else:
    print(f"{x} is less than 15")
print("I am out of scope")

if x == 15: print("really!!")  # no else

print("congratulations") if x >= 50 else print("next time inshallah!")


def adding_function(a, b=0, d=0, e=0, f=0, g=0):
    c = a + b + d + e + f + g
    return c, b + d


x, y = adding_function(2, 3, 4, 5, f=6)
print(x)
print(y)

count = 0

while count < 5:
    print(f"i am in {count}")
    count += 1
print(count)

# msg = input("enter a sentence")
#
# i = 0
#
# while i < len(msg):
#     if msg[i] == "a" or msg[i] == "i" or msg[i] == "e" or msg[i] == "o" or msg[i] == "u":
#         i += 1
#         continue
#     print(msg[i], end="")
#     i += 1

print(" ")
print(x, y, z, sep="***")

# summation = 0
#
# while True:
#     num = int(input("enter a number (enter -1 to stop):"))
#     if num == -1:
#         break
#     else:
#         summation += num
#
# print(summation)

# msg = input("enter a sentence")
#
# for ch in msg:
#     if ch not in "aieou": print(ch, end="")

print(" ")
x = [1, 2, 3, 4]

for ele in x:
    if ele % 2 == 0:
        print(ele)

for i in range(5, 30, 3):
    print(i, end=" ")

print()
l1 = [35, 30, 22, 37]
l2 = [40, 33, 40, 25, 36]
l3 = [2, 3]
result = []
for ele1, ele2, _ in zip(l1, l2, l3):
    result.append(ele1 + ele2)

print(result)

A = [5, "Nuri", True, 3.5]
print(A[0])
print(A[-1])
print(A[:2])
print(A[2:])
print(A[1:3])
print([A[1], A[-1]])
print(len(A))

for i in range(len(A)):
    print(f"ele: {i}, value:{A[i]}")

print(" ")
for i, ele in enumerate(A):
    print(f"ele: {i}, value:{ele}")

print(A.pop())
A.pop(0)
print(A)
A.reverse()
print(A)
A.insert(1, 20)
A[2] = "Ali"
print(A)

B = [[0, 1, 6], [1, 0, 3]]

print(B[1][1])
print(B[0][1:])

# list comprehension

C = [i * 5 for i in range(21) if i % 2 == 0]
print(C)
D = [i for i in range(0, 101, 10)]
print(D)
E = list("EE432")
print(E)

file = open("test.txt", "r")

for line in file:
    print(line)

file.close()

file = open("test2.txt", "w")

file.write("my first file write\n")
file.write("Done!")

file.close()


# *arg **kwargs

def fun(*args):
    su = 0
    for i in args:
        su += i
    return su


print(fun(1, 2, 3, 4))


def fun2(**kwargs):
    for k, v in kwargs.items():
        print(f"key: {k}, value: {v}")


fun2(a=3, b=True, C="Ahmed")
