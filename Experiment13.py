icode = []

print("\nEnter the set of intermediate code (terminated by 'exit'):")

# Input loop
while True:
    line = input()
    icode.append(line)
    if line == "exit":
        break

print("\nTarget Code Generation")
print("************************")

i = 0

while icode[i] != "exit":
    str_exp = icode[i]

    # Determine operator
    if len(str_exp) > 3:
        op = str_exp[3]
    else:
        op = ''

    if op == '+':
        opr = "ADD"
    elif op == '-':
        opr = "SUB"
    elif op == '*':
        opr = "MUL"
    elif op == '/':
        opr = "DIV"
    else:
        opr = ""

    # Generate assembly-like code
    try:
        print(f"\n\tMOV {str_exp[2]}, R{i}")
        if opr:
            print(f"\t{opr} {str_exp[4]}, R{i}")
        print(f"\tMOV R{i}, {str_exp[0]}")
    except IndexError:
        print(f"\nInvalid intermediate code format: {str_exp}")

    i += 1