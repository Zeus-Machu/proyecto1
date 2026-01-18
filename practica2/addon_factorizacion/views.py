from django.shortcuts import render
import sympy as sp

def factorizacion(request):
    resultado = None
    error = None

    if request.method == "POST":
        expr = request.POST.get("expresion")

        try:
            x = sp.symbols('x')

            # NORMALIZAR la expresión
            expr = expr.replace("²", "^2")
            expr = expr.replace("^", "**")
            expr = expr.replace(" ", "")
            expr = expr.replace("x", "*x").replace("**x", "*x")
            expr = expr.replace("1*x", "x")

            expresion = sp.sympify(expr)
            resultado = sp.factor(expresion)

        except Exception:
            error = "Expresión no válida. Usa una expresión algebraica con x."

    return render(request, "addon_factorizacion/factorizacion.html", {
        "resultado": resultado,
        "error": error
    })
