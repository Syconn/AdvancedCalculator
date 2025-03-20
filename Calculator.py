# Calculates the Solution to the Equation
def calculate(problem: str):
    return equation(problem.split(" "))

# PEMDAS
def find_operation(parts: list[str]):
    priority = { "(": 1, ")": 1, "*": 2, "/": 2, "+": 3, "-": 3}
    return min([(i, x) for i, x in enumerate(parts) if x in priority], key=lambda v: priority[v[1]], default=parts[0])

def equation(parts):
    while len(parts) > 1:
        op = find_operation(parts)
        parts = parts[0:op[0]-1] + [evaluate(parts, op[0])] + parts[op[0]+2:]
    return parts[0]

def evaluate(parts: list[str], spot: int) -> str:
    return str(operation(parts[spot-1:spot+2]))

def operation(op: list[str]) -> float | int:
    match op[1]:
        case "*":
            return zero(float(op[0]) * float(op[2]))
        case "/":
            return zero(float(op[0]) / float(op[2]))
        case "-":
            return zero(float(op[0]) - float(op[2]))
        case _:
            return zero(float(op[0]) + float(op[2]))

def zero(f: float) -> float | int:
    if str(f).endswith('.0'): return int(f)
    return f