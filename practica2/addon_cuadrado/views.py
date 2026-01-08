from django.shortcuts import render

def  cuadrado(request):
    resultado_area = None
    resultado_peri = None
    error = None

    if request.method == "POST":
        try:
            L = float(request.POST.get("a", "").replace(",", "."))
            
            resultado_area =  L*L
            resultado_peri =  4*L

        except ValueError:
            error = "Ingresa números válidos (puedes usar coma o punto para decimales)."

    return render(request, "addon_cuadrado/plantilla.html", {
        "resultado_area": resultado_area,
        "resultado_peri": resultado_peri,
        "error": error
    })