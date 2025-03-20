# Calculates the Solution to the Equation
import Operations

def calculate(problem: str):
    # return Operations.evaluate(problem)
    return equation(problem.split(" "))

# PEMDAS
def find_operation(parts: list[str]):
    priority = { "(": 1, ")": 1, "*": 2, "/": 2, "+": 3, "-": 3}
    return min([(i, x) for i, x in enumerate(parts) if x in priority], key=lambda v: priority[v[1]], default=parts[0])

# Recursive
def equation(parts):
    print(find_operation(parts))
    pass

if __name__ == "__main__":
    print(calculate("2 + 2 * 4"))