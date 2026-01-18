from django.shortcuts import render

def sumar(request):
    resultado = None

    if request.method == "POST":
        a = float(request.POST.get("a", 0))
        b = float(request.POST.get("b", 0))
        resultado = a + b

    return render(request, "addon_suma/sum.html", {"resultado": resultado})