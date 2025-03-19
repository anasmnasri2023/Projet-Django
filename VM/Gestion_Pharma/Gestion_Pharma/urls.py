# Gestion_Pharma/urls.py
from django.contrib import admin
from django.urls import path, include
from Produits import views  # Importer les vues de l'application Produits

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Produits/', include('Produits.urls')),  # Inclure les URLs de l'application Produits
    path('', views.Affichage.as_view(), name='home'),  # Utilisation de la classe Affichage pour l'URL ''
]
