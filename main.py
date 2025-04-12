from fastapi import FastAPI
from pydantic import BaseModel
from solver import solve_equation
from explainer import explain_solution

app = FastAPI()

class MathRequest(BaseModel):
    problem: str

@app.post("/solve")
def solve(request: MathRequest):
    solution, steps = solve_equation(request.problem)
    explanation = explain_solution(request.problem)
    return {
        "problem": request.problem,
        "solution": solution,
        "steps": steps,
        "explanation": explanation
    }