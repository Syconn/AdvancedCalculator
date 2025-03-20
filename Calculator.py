# Calculates the Solution to the Equation
import Operations

def calculate(problem: str):
    # return Operations.evaluate(problem)
    return equation(problem.split(" "))

# PEMDAS
def find_operation(parts: list[str]):
    priority = { "(": 1, ")": 1, "*": 2, "/": 2, "+": 3, "-": 3}
    return min([(i, x) for i, x in enumerate(parts) if x in priority], key=lambda v: priority[v[1]], default=parts[0])

def equation(parts):
    while len(parts) > 1:
        op = find_operation(parts)
        parts = parts[0:op[0]-1] + [Operations.evaluate(parts, op[0])] + parts[op[0]+2:]
    return parts[0]

if __name__ == "__main__":
    print(calculate("2 + 2 / 2 * 4"))