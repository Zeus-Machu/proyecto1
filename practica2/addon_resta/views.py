from django.shortcuts import render

def restar(request):
    resultado = None

    if request.method == "POST":
        a = int(request.POST.get("a", 0))
        b = int(request.POST.get("b", 0))
        resultado = a - b

    return render(request, "addon_resta/res.html", {"resultado": resultado})