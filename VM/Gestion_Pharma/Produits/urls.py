from django.urls import path
from Produits.views import Affichage

urlpatterns = [
    path('', Affichage.as_view(), name='home'),
]
