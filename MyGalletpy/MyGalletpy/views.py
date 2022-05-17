from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
import os
from MyGalletpy.settings import BASE_DIR
# Necesitamos Request para realizar peticiones al servidor
# Necesitamos HttpResponse Enviar respuesta por medio del protocolo HTTP

#Vista del home de la aplicacion
def home(request): #Se le pasa un objeto de tipo request como primer argumento
    return render(request, "home_template.html")

def pockets(request):
    return render(request, "pocket_template.html")

def login(request):
    return render(request, "login_template.html")

def register(request):
    return render(request, "register_template.html")

def history(request):
    return render(request, "history_template.html")

def transaction(request):
    return render(request, "transaction_template.html")