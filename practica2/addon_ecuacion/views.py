from django.shortcuts import render
import math

def ecuacion(request):
    x1 = None
    x2 = None
    error = None

    if request.method == "POST":
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')

        # Verificar que no estén vacíos
        if a == "" or b == "" or c == "":
            error = "Todos los campos son obligatorios"
        else:
            a = float(a)
            b = float(b)
            c = float(c)

            raiz = (b * b) - ((4 * a) * c)

            if raiz < 0:
                error = "La raiz es menor que 0"
            else:
                x1 = (-b + math.sqrt(raiz)) / (2 * a)
                x2 = (-b - math.sqrt(raiz)) / (2 * a)

    return render(request, 'addon_ecuacion/ecuacion.html', {
        'x1': x1,
        'x2': x2,
        'error': error
    })