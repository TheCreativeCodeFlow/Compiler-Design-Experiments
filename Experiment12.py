# Intermediate Code Generation in Python

str_exp = ""
left = ""
right = ""
tmpch = ord('Z')  # ASCII value for temporary variables

# structure equivalent
class Exp:
    def __init__(self, pos, op):
        self.pos = pos
        self.op = op

k = []


def findopr():
    global str_exp, k
    operators = [':', '/', '*', '+', '-']
    for op in operators:
        for i in range(len(str_exp)):
            if str_exp[i] == op:
                k.append(Exp(i, op))


def fleft(x):
    global str_exp
    w = 0
    flag = False
    left = ""

    x -= 1
    while x != -1 and str_exp[x] not in ['+', '*', '=', '/', ':']:
        if str_exp[x] != '$' and not flag:
            left += str_exp[x]
            str_exp = str_exp[:x] + '$' + str_exp[x+1:]
            flag = True
        x -= 1

    return left[::-1]  # reverse since collected backwards


def fright(x):
    global str_exp
    w = 0
    flag = False
    right = ""

    x += 1
    while x < len(str_exp) and str_exp[x] not in ['+', '*', '=', '/', ':']:
        if str_exp[x] != '$' and not flag:
            right += str_exp[x]
            str_exp = str_exp[:x] + '$' + str_exp[x+1:]
            flag = True
        x += 1

    return right


def explore():
    global tmpch, str_exp

    i = 0
    print("\nThe intermediate code:\t\tExpression")

    while i < len(k):
        pos = k[i].pos

        left = fleft(pos)
        right = fright(pos)

        temp = chr(tmpch)
        tmpch -= 1

        str_exp = str_exp[:pos] + temp + str_exp[pos+1:]

        print(f"\t{temp} := {left}{k[i].op}{right}\t\t", end="")

        for ch in str_exp:
            if ch != '$':
                print(ch, end="")
        print()

        i += 1

    # Final assignment
    final_right = fright(-1)
    final_left = fleft(len(str_exp))

    print(f"\t{final_right} := {final_left}")


# Main program
print("\t\tINTERMEDIATE CODE GENERATION\n")
str_exp = input("Enter the Expression: ")

findopr()
explore()