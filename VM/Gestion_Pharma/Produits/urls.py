from django.urls import path
from .views import * 

urlpatterns = [
    path('produit/', Affichage.as_view(), name='home'),
     path('produit/modifier/<int:pk>/', views.modifier_produit, name='modifier'),
    
    # URL pour supprimer un produit
    path('produit/supprimer/<int:pk>/', views.supprimer_produit, name='delete'),
    
    # URL pour voir les détails d'un produit
    path('produit/details/<int:pk>/', views.details_produit, name='details'),
]