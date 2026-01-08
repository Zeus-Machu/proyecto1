from django.shortcuts import render

def rectangulo(request):
    resultado_area = None
    resultado_peri = None
    error = None

    if request.method == "POST":
        try:
            B = float(request.POST.get("a", "").replace(",", "."))
            H = float(request.POST.get("b", "").replace(",", "."))
            
            resultado_area =  B*H
            resultado_peri =  (2*B)+(2*H)

        except ValueError:
            error = "Ingresa números válidos (puedes usar coma o punto para decimales)."

    return render(request, "addon_rectangulo/plantilla.html", {
        "resultado_area": resultado_area,
        "resultado_peri": resultado_peri,
        "error": error
    })