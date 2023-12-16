from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def login_ren(request):

    return render(request, 'fomularioInicio.html')