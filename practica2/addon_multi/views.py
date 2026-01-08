from django.shortcuts import render

def multiplicacion(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.POST.get("a", "").replace(",", "."))
            b = float(request.POST.get("b", "").replace(",", "."))

            resultado = a * b  # ← Aquí sí se puede multiplicar por 0 sin restricciones

        except ValueError:
            error = "Ingresa números válidos (puedes usar coma o punto para decimales)."

    return render(request, "addon_multi/plantilla.html", {
        "resultado": resultado,
        "error": error
    })