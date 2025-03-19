from django.urls import path
from .views import * 

urlpatterns = [
    path('produit/', Affichage.as_view(), name='home'),
    
]