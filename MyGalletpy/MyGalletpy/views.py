from django.shortcuts import render
# Need Request to make querys to the server
# Need HttpResponse to send response using HTTP protocol, now using render shortcut for the same functionality

#application's home view 
def home(request): #Takes a request object as parameter
    # render function takes a request object as first argument
    # As second argument it takes a string specifying the name of the template thats gonna be used
    # As a third and optional argument it takes a dictionary as a context parameter for the template 
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