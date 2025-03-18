from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

# def home(request):

#recuperation des données
  #  donnees = Produits.objects.all()

   # context = {
    #    'donnees': donnees
    # }

    # # return render(request, 'home.html' , context)

class Affichage( ListView):

    # Affichage du template
    template_name = 'home.html'
    # Récupération des données
    queryset = Produits.objects.all()