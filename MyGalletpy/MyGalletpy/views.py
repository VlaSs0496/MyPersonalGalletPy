from django.http import HttpResponse
from django.template import Template, Context
# Necesitamos Request para realizar peticiones al servidor
# Necesitamos HttpResponse Enviar respuesta por medio del protocolo HTTP

#Vista del home de la aplicacion
def home(request): #Se le pasa un objeto de tipo request como primer argumento
    externalTemplate = open("C:/Users/User/Desktop/Cosas universidad/Semestre 4/Lab de software III/Corte 2/My personal wallet/MyPersonalGalletPy/MyGalletpy/MyGalletpy/templates/home_view_template/home_template.html")
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def pockets(request):
    externalTemplate = open("C:/Users/User/Desktop/Cosas universidad/Semestre 4/Lab de software III/Corte 2/My personal wallet/MyPersonalGalletPy/MyGalletpy/MyGalletpy/templates/pockets_view_template/pocket_template.html")
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def login(request):
    externalTemplate = open("C:/Users/User/Desktop/Cosas universidad/Semestre 4/Lab de software III/Corte 2/My personal wallet/MyPersonalGalletPy/MyGalletpy/MyGalletpy/templates/login_view_template/login_template.html")
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def register(request):
    externalTemplate = open("C:/Users/User/Desktop/Cosas universidad/Semestre 4/Lab de software III/Corte 2/My personal wallet/MyPersonalGalletPy/MyGalletpy/MyGalletpy/templates/register_view_template/register_template.html")
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def history(request):
    externalTemplate = open("C:/Users/User/Desktop/Cosas universidad/Semestre 4/Lab de software III/Corte 2/My personal wallet/MyPersonalGalletPy/MyGalletpy/MyGalletpy/templates/history_view_template/history_template.html")
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def transaction(request):
    externalTemplate = open("C:/Users/User/Desktop/Cosas universidad/Semestre 4/Lab de software III/Corte 2/My personal wallet/MyPersonalGalletPy/MyGalletpy/MyGalletpy/templates/transaction_view_template/transaction_template.html")
    template = Template(externalTemplate.read())
    externalTemplate.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)