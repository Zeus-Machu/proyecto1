from django.shortcuts import render

def ecuacion_primera(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.POST.get("a"))
            b = float(request.POST.get("b"))

            if a == 0:
                error = "El coeficiente 'a' no puede ser 0."
            else:
                resultado = -b / a

        except:
            error = "Datos inválidos."

    return render(request, "addon_primera/ecuacion.html", {
        "resultado": resultado,
        "error": error
    })
