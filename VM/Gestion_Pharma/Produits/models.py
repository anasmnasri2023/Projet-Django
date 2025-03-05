from django.db import models

# Modèle des catégories
class Categories(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


# Modèle des produits
class Produits(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="produits")
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Utilisation de DecimalField pour les prix
    quantite = models.PositiveIntegerField(default=0)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField()
    # Si vous souhaitez gérer les images, décommentez la ligne suivante
    # image = models.ImageField(null=True, blank=True, upload_to="media/")

    class Meta:
        ordering = ["date_ajout"]  # Tri des produits par date d'ajout

    def status_quantite(self):
        """Retourne une couleur en fonction du stock disponible."""
        if self.quantite == 0:
            return "red"  # Indique que le produit est en rupture de stock
        elif self.quantite <= 10:
            return "orange"  # Indique que le stock est faible
        else:
            return "green"  # Indique que le stock est suffisant

    def __str__(self):
        return f"{self.name} ({self.quantite} en stock)"


# Modèle des clients
class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Modèle des ventes
class Vente(models.Model):
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE, related_name="ventes")
    sale_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="ventes")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vente de {self.quantity} {self.produit.name} à {self.customer.name}"


# Modèle des factures clients
class FactureClient(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="factures")
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE, related_name="factures")
    quantite = models.PositiveIntegerField()
    date_achat = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Facture de {self.customer.name} - {self.produit.name} ({self.quantite} pcs)"
