from sympy import symbols, Eq, solve, simplify
from sympy.parsing.sympy_parser import parse_expr

def solve_equation(problem: str):
    try:
        x = symbols('x')
        left, right = problem.split('=')
        equation = Eq(parse_expr(left), parse_expr(right))
        solution = solve(equation)
        steps = [
            f"Start with: {problem}",
            f"Rearrange: {simplify(left)} = {simplify(right)}",
            f"Solve: x = {solution}"
        ]
        return str(solution), steps
    except Exception as e:
        return "Error", [str(e)]