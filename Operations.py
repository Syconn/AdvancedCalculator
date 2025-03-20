def evaluate(expr: str) -> str:
    return str(operation(expr.split(" ")))

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
