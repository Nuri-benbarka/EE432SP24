from stack import StackLL, StackArr


#Q1 _________________________
# user_str = input("Enter a string")
#
# my_stack = StackLL()
#
# for c in user_str:
#     my_stack.push(c)
#
# output_str = ""
#
# while len(my_stack) > 0:
#     output_str += my_stack.pop()
#
# print(output_str)
def check_balanced(str):
    my_stack = StackArr(10)
    for c in user_eq:
        if c == "(":
            my_stack.push(c)
        elif c == ")":
            v = my_stack.pop()
            if v == "Stack underflow":
                return False

    if len(my_stack) == 0:
        return True
    else:
        return False


def polish_notation(user_str):
    my_stack = StackArr(10)

    user_str = user_str.split(" ")
    output_list = []

    for ele in user_str:
        if ele in "+-*/":
            if len(my_stack) == 0:
                my_stack.push(ele)
            elif my_stack.top() in "*/" and ele in "+-":
                while len(my_stack) > 0:
                    output_list.append(my_stack.pop())
                my_stack.push(ele)
            else:
                my_stack.push(ele)
        else:
            output_list.append(ele)

    while len(my_stack) > 0:
        output_list.append(my_stack.pop())

    return output_list


#user_eq = input("Enter your equation")

#print(check_balanced(user_eq))
#print(polish_notation(user_eq))


def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1


def associativity(c):
    if c == '^':
        return 'R'
    return 'L'  # Default to left-associative


def infix_to_postfix(s):
    result = []
    stack = []

    for i in range(len(s)):
        c = s[i]

        # If the scanned character is an operand, add it to the output string.
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            result.append(c)
        # If the scanned character is an ‘(‘, push it to the stack.
        elif c == '(':
            stack.append(c)
        # If the scanned character is an ‘)’, pop and add to the output string from the stack
        # until an ‘(‘ is encountered.
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop '('
        # If an operator is scanned
        else:
            while stack and (prec(s[i]) < prec(stack[-1]) or
                             (prec(s[i]) == prec(stack[-1]) and associativity(s[i]) == 'L')):
                result.append(stack.pop())
            stack.append(c)

    # Pop all the remaining elements from the stack
    while stack:
        result.append(stack.pop())

    print(''.join(result))


def simple_op(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "^":
        return num1 ** num2


def excute_exp(post):
    my_stack = StackArr(10)
    for ele in post:
        if ele in "+-*/^":
            num2 = my_stack.pop()
            num1 = my_stack.pop()
            my_stack.push(simple_op(ele, num1, num2))
        else:
            my_stack.push(int(ele))
    return my_stack.pop()


# Driver code
exp = "a+b*(c^d-e)^(f+g*h)-i"

# Function call
infix_to_postfix(exp)

print(excute_exp(["2", "3", "4", "*", "5", "-", "6", "/", "+"]))
