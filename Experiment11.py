
# Intermediate Code Generation: Quadruple, Triple, Indirect Triple
# Expression: a = b + c * d

def generate_quadruple():
    print("=== Quadruple Representation ===")
    quadruples = [
        ("*", "c", "d", "t1"),
        ("+", "b", "t1", "t2"),
        ("=", "t2", "-", "a")
    ]
    for q in quadruples:
        print(q)
    return quadruples


def generate_triple():
    print("\n=== Triple Representation ===")
    triples = [
        ("*", "c", "d"),      # index 0
        ("+", "b", "(0)"),    # refers to result of index 0
        ("=", "(1)", "a")     # refers to result of index 1
    ]
    for i, t in enumerate(triples):
        print(f"{i}: {t}")
    return triples


def generate_indirect_triple(triples):
    print("\n=== Indirect Triple Representation ===")
    pointer_table = [0, 1, 2]  # referencing triples

    for i in pointer_table:
        print(f"{i}: {triples[i]}")


def main():
    quad = generate_quadruple()
    triples = generate_triple()
    generate_indirect_triple(triples)


if __name__ == "__main__":
    main()

