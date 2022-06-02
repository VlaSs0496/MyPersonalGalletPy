import sys
sys.path.append("..")

from django.shortcuts import redirect, render
from .prueba import Prueba
from users.models import User, Transaction, Normal_transaction, Pocket_transaction, Pocket
from .forms import LoginForm, RegisterForm, TransactionForm, PocketCreationForm

usernameGlobal = ''
idGlobal = -1

# Need Request to make querys to the server
# Need HttpResponse to send response using HTTP protocol, now using render shortcut for the same functionality

#application's home view 
def home(request): #Takes a request object as parameter
    # render function takes a request object as first argument
    # As second argument it takes a string specifying the name of the template thats gonna be used
    # As a third and optional argument it takes a dictionary as a context parameter for the template 
    saldo = calculoSaldo()
    return render(request, "home_template.html",{'saldo':saldo})


def pockets(request):
    pocketlist = Pocket.objects.all().filter(id_user_id = globals()['idGlobal'])
    return render(request, "pocket_template.html", {'list':pocketlist})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("entra")
            username = form.cleaned_data['username_field_login']
            password = form.cleaned_data['password_field_login']

            if validationLogin(username, password):
                saldo = calculoSaldo()
                return render(request, "home_template.html", {'saldo':saldo})

    return render(request, "login_template.html")

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username_field']
            password = form.cleaned_data['password_field']

            if validationRegister(username):
                newUser = User(username=username, password=password)
                newUser.save()
                return render(request, "home_template.html", {'username':username})

    return render(request, "register_template.html")

def history(request):

    transactions = Transaction.objects.raw(f"SELECT * FROM public.users_normal_transaction as nt INNER JOIN public.users_transaction ON id_transaction_id = id_transaction WHERE nt.id_user_id = {globals()['idGlobal']}")
    return render(request, "history_template.html", {"lista": transactions})

def transaction(request):
    if request.method == 'POST':
        validationTransaction(request)
    
    pockets = Pocket.objects.all().filter(id_user_id = globals()['idGlobal'])

    return render(request, "transaction_template.html", {"opciones": pockets})

def pocket_creation(request):
    if request.method == 'POST':
        form = PocketCreationForm(request.POST)
        if form.is_valid():
            pocket_name = form.cleaned_data['pocket_creation_name']
            nuevoPocket = Pocket(name_pocket = pocket_name, id_user_id = globals()['idGlobal'], balance_pocket=0.0)
            nuevoPocket.save()

    return render(request, 'pockets_creation_template.html')

def validationRegister(username):
    users = User.objects.all()
    for user in users:
        if user.username == username:
            return False
    return True

def validationLogin(username, password):
    users = User.objects.all()
    for user in users:
        if user.username == username and user.password == password:
            print(f"entra {username} {password}")
            globals()['usernameGlobal']  = username
            globals()['idGlobal'] = user.id_user
            return True

    return False

def calculoSaldo():
    saldo = 0.0
    transactions = Transaction.objects.all().filter(id_user_id = globals()['idGlobal'])
    for transaction in transactions:
        if transaction.type_transaction == True:
            saldo += float(transaction.amount) 
        else:
            saldo -= float(transaction.amount)

    return saldo

def validationTransaction(request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            print('llega')
            transaction_amount = form.cleaned_data['transaction_amount']
            transaction_reason = form.cleaned_data['transaction_reason']
            transaction_date = form.cleaned_data['transaction_date']
            transaction_type = form.cleaned_data['transaction_type']
            transaction_behavior = form.cleaned_data['transaction_behavior']
            transaction_pocket = form.cleaned_data['transaction_pocket']

            newTransaction = Transaction(id_user_id = globals()['idGlobal'], amount = transaction_amount,
             date_transaction=transaction_date, type_transaction=transaction_behavior)
            newTransaction.save()
            idTransaction = newTransaction.id_transaction

            if transaction_type == 'True':
                print(type(transaction_type))
                newNormalTransaction = Normal_transaction(description = transaction_reason, id_transaction_id = idTransaction, 
                id_user_id = globals()['idGlobal'])
                newNormalTransaction.save()
            else:
                print('Se hace esta mierda')
                pockets = Pocket.objects.get(name_pocket=transaction_pocket)
                pocketTransaction = Pocket_transaction(id_pocket = pockets.id_pocket, id_transaction_id = idTransaction)
                pocketTransaction.save()

                pocket1 = Pocket.objects.get(id_pocket = pockets.id_pocket)
                pocket2 = Pocket.objects.all().filter(id_pocket=pockets.id_pocket).update(balance_pocket = (pocket1.balance_pocket + float(transaction_amount)))
