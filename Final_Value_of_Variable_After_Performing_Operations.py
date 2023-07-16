def finalValueAfterOperations(self, operations: list[str]) -> int:
    #for sake of an algorithm
    value = 0

    for op in operations:
        if op[0] == "-" or op[1] == "-":
            value -= 1
        else:
            value += 1

    #Or simple generator expression
    #return sum(1 if "+" in op else -1 for op in operations)