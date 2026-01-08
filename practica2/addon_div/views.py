from django.shortcuts import render

def divicion(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            # Tomamos las cadenas, quitamos espacios y cambiamos coma por punto
            raw_a = request.POST.get("a", "").strip().replace(",", ".")
            raw_b = request.POST.get("b", "").strip().replace(",", ".")

            if raw_a == "" or raw_b == "":
                raise ValueError("Faltan valores.")

            a = float(raw_a)
            b = float(raw_b)

            # Considerar números extremadamente pequeños como 0 para evitar división errónea
            if abs(b) < 1e-12:
                error = "No se puede dividir entre 0."
            else:
                resultado = a / b

        except ValueError:
            error = "Ingresa solo números válidos (puedes usar coma o punto para decimales)."

    return render(request, "addon_div/plantilla.html", {
        "resultado": resultado,
        "error": error
    })

