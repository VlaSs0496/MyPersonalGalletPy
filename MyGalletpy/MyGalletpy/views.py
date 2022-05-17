from django.http import HttpResponse
from django.template import Template, Context
import os
from MyGalletpy.settings import BASE_DIR
# Necesitamos Request para realizar peticiones al servidor
# Necesitamos HttpResponse Enviar respuesta por medio del protocolo HTTP

#Vista del home de la aplicacion
def home(request): #Se le pasa un objeto de tipo request como primer argumento
    file_path = os.path.join(BASE_DIR, "MyGalletPy/templates/home_view_template/home_template.html")
    externalTemplate = open(file_path)
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def pockets(request):
    file_path = os.path.join(BASE_DIR, "MyGalletPy/templates/pockets_view_template/pocket_template.html")
    externalTemplate = open(file_path)
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def login(request):
    file_path = os.path.join(BASE_DIR, "MyGalletPy/templates/login_view_template/login_template.html")
    externalTemplate = open(file_path)
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def register(request):
    file_path = os.path.join(BASE_DIR, "MyGalletPy/templates/register_view_template/register_template.html")
    externalTemplate = open(file_path)
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def history(request):
    file_path = os.path.join(BASE_DIR, "MyGalletPy/templates/history_view_template/history_template.html")
    externalTemplate = open(file_path)
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def transaction(request):
    file_path = os.path.join(BASE_DIR, "MyGalletPy/templates/transaction_view_template/transaction_template.html")
    externalTemplate = open(file_path)
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)