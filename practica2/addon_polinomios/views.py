from django.shortcuts import render
from sympy import sympify, pretty, latex

def calcular(request):
    resultado = ""
    error = ""

   
    if request.method == 'POST':
        polinomio1 = request.POST.get('polinomio1', '').strip()
        polinomio2 = request.POST.get('polinomio2', '').strip()
        operacion = request.POST.get('operacion')

        try:
            # Convertir texto a polinomios (detecta variables automáticamente)
            p1 = sympify(polinomio1)
            p2 = sympify(polinomio2)

            # Operaciones
            if operacion == 'suma':
                resultado = p1 + p2
            elif operacion == 'resta':
                resultado = p1 - p2
            elif operacion == 'multiplicacion':
                resultado = p1 * p2
            elif operacion == 'division':
                if p2 == 0:
                    raise ZeroDivisionError("No se puede dividir entre 0")
                resultado = p1 / p2

            # Simplificar resultado
            resultado = resultado.simplify()
            resultado = latex(resultado)
            

        except Exception as e:
            error = f"Entrada inválida: {e}"
    


    return render(request, 'addon_polinomio/polino.html', {
        'resultado': resultado,
        'error': error
    })


