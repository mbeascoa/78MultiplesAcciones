from django.shortcuts import render


def index(request):
    return render(request, "deportes/MultiplesAcciones.html")


def calcular(request):
    dato = request.POST['operacion']
    num1 = int(request.POST['numero1'])
    num2 = int(request.POST['numero2'])

    if dato == 'sumarNumeros':
        resultado = num1 + num2
        operacion = "SUMA"
    else:
        resultado = num1 * num2
        operacion = "MULTIPLICACIÓN"

    lista = {
        "operacion": operacion,
        "resultado": resultado

    }

    return render(request, "accionesboton/MultiplesAcciones.html", lista)


