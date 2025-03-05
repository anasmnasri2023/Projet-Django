from django.shortcuts import render
from django.views.generic import ListView
from .models import Produits

# Classe pour afficher la liste des produits
class Affichage(ListView):
    # Définir le template à utiliser
    template_name = "home.html"
    
    # Récupérer toutes les instances de Produits
    queryset = Produits.objects.all()

    # Définir le nom du contexte pour accéder aux données dans le template
    context_object_name = 'produits'

    # Ajouter la pagination
    paginate_by = 10  # Limite de 10 produits par page
