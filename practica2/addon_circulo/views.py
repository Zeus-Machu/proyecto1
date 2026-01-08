from django.shortcuts import render

def  circulo(request):
    resultado_area = None
    resultado_peri = None
    error = None

    if request.method == "POST":
        try:
            radio = float(request.POST.get("a", "").replace(",", "."))
            
            resultado_area =  3.1416 * radio**2
            resultado_peri =   2*3.1416*radio

        except ValueError:
            error = "Ingresa números válidos (puedes usar coma o punto para decimales)."

    return render(request, "addon_circulo/plantilla.html", {
        "resultado_area": resultado_area,
        "resultado_peri": resultado_peri,
        "error": error
    })