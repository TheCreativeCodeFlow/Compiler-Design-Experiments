# Data Flow & Control Flow Analysis in Python

class Expr:
    def __init__(self, op, op1, op2, res):
        self.op = op
        self.op1 = op1
        self.op2 = op2
        self.res = res
        self.flag = 0  # 0 = active, 1 = eliminated


arr = []
n = 0


def input_data():
    global n, arr
    n = int(input("\nEnter the maximum number of expressions: "))
    print("\nEnter the input (op op1 op2 result):")

    for _ in range(n):
        op = input().strip()
        op1 = input().strip()
        op2 = input().strip()
        res = input().strip()
        arr.append(Expr(op, op1, op2, res))


def is_number(x):
    return x.isdigit()


def change(p, q, res):
    global arr, n
    for i in range(q + 1, n):
        if arr[q].res == arr[i].op1:
            arr[i].op1 = arr[p].res if res is None else res
        elif arr[q].res == arr[i].op2:
            arr[i].op2 = arr[p].res if res is None else res


def constant():
    global arr
    for i in range(n):
        if is_number(arr[i].op1) and is_number(arr[i].op2):
            op1 = int(arr[i].op1)
            op2 = int(arr[i].op2)
            op = arr[i].op

            if op == '+':
                res = op1 + op2
            elif op == '-':
                res = op1 - op2
            elif op == '*':
                res = op1 * op2
            elif op == '/':
                res = op1 // op2 if op2 != 0 else 0
            else:
                continue

            arr[i].flag = 1
            change(i, i, str(res))


def expression():
    global arr
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i].op == arr[j].op:
                if arr[i].op in ['+', '*']:  # commutative
                    if ((arr[i].op1 == arr[j].op1 and arr[i].op2 == arr[j].op2) or
                        (arr[i].op1 == arr[j].op2 and arr[i].op2 == arr[j].op1)):
                        arr[j].flag = 1
                        change(i, j, None)
                else:
                    if arr[i].op1 == arr[j].op1 and arr[i].op2 == arr[j].op2:
                        arr[j].flag = 1
                        change(i, j, None)


def output():
    print("\nOptimized code is:")
    for i in range(n):
        if arr[i].flag == 0:
            print(arr[i].op, arr[i].op1, arr[i].op2, arr[i].res)


# Main
input_data()
constant()
expression()
output()