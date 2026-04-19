
# Stack Storage Allocation Simulation (Compiler Concept)

class StackFrame:
    def __init__(self, function_name, local_vars):
        self.function_name = function_name
        self.local_vars = local_vars  # dictionary of variables

    def __str__(self):
        return f"{self.function_name} -> {self.local_vars}"


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, frame):
        print(f"\n[CALL] {frame.function_name}()")
        self.stack.append(frame)
        self.display()

    def pop(self):
        if self.stack:
            frame = self.stack.pop()
            print(f"\n[RETURN] {frame.function_name}()")
            self.display()
            return frame
        else:
            print("Stack Underflow")

    def display(self):
        print("\nCurrent Stack:")
        if not self.stack:
            print("Empty")
        else:
            for i in reversed(range(len(self.stack))):
                print(f"  {self.stack[i]}")


# Simulating function calls using stack allocation

def function_A(stack):
    frame_A = StackFrame("A", {"x": 10, "y": 20})
    stack.push(frame_A)

    function_B(stack)

    stack.pop()


def function_B(stack):
    frame_B = StackFrame("B", {"p": 5})
    stack.push(frame_B)

    function_C(stack)

    stack.pop()


def function_C(stack):
    frame_C = StackFrame("C", {"z": 100})
    stack.push(frame_C)

    # No further calls
    stack.pop()


def main():
    runtime_stack = Stack()
    function_A(runtime_stack)


if __name__ == "__main__":
    main()

