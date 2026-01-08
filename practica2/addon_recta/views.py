from django.shortcuts import render

def recta(request):
    numeros = None
    error = None

    if request.method == "POST":
        inicio = int(request.POST.get("inicio"))
        fin = int(request.POST.get("fin"))

        if inicio <= fin:
            numeros = range(inicio, fin + 1)
        else:
            error = "El valor final debe ser mayor o igual al inicial"

    return render(request, "addon_recta/plantilla.html", {
        "numeros": numeros,
        "error": error
    })