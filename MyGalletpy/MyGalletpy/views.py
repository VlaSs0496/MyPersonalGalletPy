from django.http import HttpResponse
from django.template import Template, Context, loader
import os
from MyGalletpy.settings import BASE_DIR
# Necesitamos Request para realizar peticiones al servidor
# Necesitamos HttpResponse Enviar respuesta por medio del protocolo HTTP

#Vista del home de la aplicacion
def home(request): #Se le pasa un objeto de tipo request como primer argumento
    externalTemplate = loader.get_template("home_template.html")
    document = externalTemplate.render()
    return HttpResponse(document)

def pockets(request):
    externalTemplate = loader.get_template("pockets_template.html")
    document = externalTemplate.render()
    return HttpResponse(document)

def login(request):
    externalTemplate = loader.get_template("login_template.html")
    document = externalTemplate.render()
    return HttpResponse(document)

def register(request):
    externalTemplate = loader.get_template("register_template.html")
    document = externalTemplate.render()
    return HttpResponse(document)

def history(request):
    externalTemplate = loader.get_template("history_template.html")
    document = externalTemplate.render()
    return HttpResponse(document)

def transaction(request):
    externalTemplate = loader.get_template("transaction_template.html")
    document = externalTemplate.render()
    return HttpResponse(document)