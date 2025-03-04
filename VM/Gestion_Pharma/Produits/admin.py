from django.contrib import admin

from .models import *

admin.site.register(Categories)
admin.site.register(Produits)
admin.site.register(Customer)
admin.site.register(Vente)
admin.site.register(FactureClient)
# Register your models here.
