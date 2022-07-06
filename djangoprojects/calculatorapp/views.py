from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'input.html')


def addition(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a + b

        return render(request, "result.html", {"result": res})

    else:
        a = float(num1)
        b = float(num2)
        if isinstance(a, float) and isinstance(b, float):
            res = a + b

            return render(request, "result.html", {"result": res})


def subtraction(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a - b
        return render(request, "result.html", {"result": res})
    else:
        a = float(num1)
        b = float(num2)
        if isinstance(a, float) and isinstance(b, float):
            res = a - b

            return render(request, "result.html", {"result": res})


def multiplication(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a * b
        return render(request, "result.html", {"result": res})
    else:
        a = float(num1)
        b = float(num2)
        if isinstance(a, float) and isinstance(b, float):
            res = a * b

            return render(request, "result.html", {"result": res})


def division(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        if b == 0:
            res = "Zero divide error"
            return render(request, "result.html", {"result": res})
        else:
            res = a / b
            return render(request, "result.html", {"result": res})

    else:
        a = float(num1)
        b = float(num2)
        if isinstance(a, float) and isinstance(b, float):
            if b == 0:
                res = "Zero divide error"
                return render(request, "result.html", {"result": res})
            else:
                res = a / b
                return render(request, "result.html", {"result": res})
