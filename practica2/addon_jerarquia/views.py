from django.shortcuts import render
import sympy as sp

def jerarquia_operaciones(request):
    resultado = None
    error = None

    if request.method == "POST":
        expresion = request.POST.get("expresion")

        try:
            resultado = sp.sympify(expresion)
        except:
            error = "Expresión inválida. Usa operadores correctos."

    return render(request, "jerarquia.html", {
        "resultado": resultado,
        "error": error
    })
