import datetime

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Abonnement, Client, Equipment, Coach, Offre
from .utils import check_abonnement
from .forms import AbonnementForm, LoginForm


# Create your views here.


def Logout(request):
    logout(request)
    return redirect('login')


def Login(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('home')

            else:
                messages.success(request, "Nom d'utilisateur ou mot de passe incorrect !")
    return render(request, 'login.html', context={'form': form})


@login_required(login_url='login')
def HomeView(request):
    check_abonnement()
    form = AbonnementForm()
    offres = Offre.objects.all()
    abonnements = Abonnement.objects.all()
    abonnement_add = None
    abonnement = None
    nbr_equipement = Equipment.objects.all().count()
    nbr_client = Client.objects.all().count()
    nbr_coach = Coach.objects.all().count()

    if request.method == "POST":
        if request.POST.get('save'):
            form = AbonnementForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Abonnement ajouté avec succes !")
                return redirect('home')
            else:
                form = AbonnementForm()
        if request.POST.get('save_ab'):
            name = request.POST.get('offre')
            offre = Offre.objects.get(type=name)
            id = request.POST.get('id_ab')
            abonnement = Abonnement.objects.get(id=id)
            abonnement.date = datetime.datetime.now()
            abonnement.offer = offre
            abonnement.save()
            messages.success(request, "Réabonnement fait avec succes !")
            return redirect('home')
    if request.GET.get('reab'):
        id_ab = request.GET.get('id_ab')
        abonnement = Abonnement.objects.get(id=id_ab)
    context = {'form': form, 'abonnement': abonnement, 'offres': offres, 'abonnements': abonnements, 'nbr_equipement': nbr_equipement, 'nbr_client': nbr_client, 'nbr_coach': nbr_coach}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def ClientView(request):
    clients = Client.objects.all()
    client = None
    client_update = None
    if request.method == "POST":
        if request.POST.get('save'):
            name = request.POST.get('nom')
            phone = request.POST.get('phone')
            adresse = request.POST.get('adresse')
            Client.objects.create(name=name, phone=phone, address=adresse)
            messages.success(request, "Client ajouté avec succes !")

            return redirect('client')
        if request.POST.get('delete'):
            id = request.POST.get('id_eq')
            client = Client.objects.get(id=id)
            client.delete()
            messages.success(request, "Client supprimé avec succes !")
            return redirect('client')

        if request.POST.get('save_update'):
            id = request.POST.get('id_eq')
            client = Client.objects.get(id=id)
            client.name = request.POST.get('nom')
            client.phone = request.POST.get('phone')
            client.address = request.POST.get('adresse')
            client.save()
            messages.success(request, "Client modifié avec succes !")
            return redirect('client')

    if request.GET.get('del'):
        id = request.GET.get('id_eq')
        client = Client.objects.get(id=id)

    if request.GET.get('edit'):
        id = request.GET.get('id_eq')
        client_update = Client.objects.get(id=id)

    context = {'clients': clients, 'client1': client, 'client_update': client_update}
    return render(request, 'client.html', context)


@login_required(login_url='login')
def EquipementView(request):
    equipements = Equipment.objects.all()
    equipement = None
    equipement_update = None
    if request.method == "POST":
        if request.POST.get('save'):
            name = request.POST.get('nom')
            desc = request.POST.get('desc')
            qts = request.POST.get('qts')
            Equipment.objects.create(name=name, description=desc, quantity=qts)
            messages.success(request, "Equipement ajouté avec succes !")

            return redirect('equipement')
        if request.POST.get('delete'):
            id = request.POST.get('id_eq')
            equipement = Equipment.objects.get(id=id)
            equipement.delete()
            messages.success(request, "Equipement supprimé avec succes !")
            return redirect('equipement')

        if request.POST.get('save_update'):
            id = request.POST.get('id_eq')
            equipement = Equipment.objects.get(id=id)
            equipement.quantity += int(request.POST.get('qts'))
            equipement.save()
            messages.success(request, "Ajouté en stock avec succes !")
            return redirect('equipement')

    if request.GET.get('del'):
        id = request.GET.get('id_eq')
        equipement = Equipment.objects.get(id=id)

    if request.GET.get('add_stock'):
        id = request.GET.get('id_eq')
        equipement_update = Equipment.objects.get(id=id)

    context = {'equipements': equipements, 'equipement1': equipement, 'equipement_update': equipement_update}
    return render(request, 'equipement.html', context)
