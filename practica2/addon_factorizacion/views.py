from django.shortcuts import render
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

def factorizacion(request):
    resultado = None
    error = None

    if request.method == "POST":
        expr = request.POST.get("expresion", "")

        try:
            x = sp.symbols('x')

            # Transformaciones para aceptar 2x, 3(x+1), etc.
            transformations = standard_transformations + (
                implicit_multiplication_application,
            )

            expr = expr.replace("²", "^2")
            expr = expr.replace("^", "**")

            expresion = parse_expr(
                expr,
                transformations=transformations,
                local_dict={"x": x}
            )

            resultado = sp.factor(expresion)

        except Exception:
            error = "Expresión no válida. Usa una expresión algebraica con x."

    return render(request, "addon_factorizacion/factorizacion.html", {
        "resultado": resultado,
        "error": error
    })
