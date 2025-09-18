from django.db import models

# Modele contenant tous les typres de champs
class Test(models.Model):
    # champs numeriques
    id = models.AutoField(primary_key=True) # Identifiant automatique
    grand_nombre = models.BigIntegerField() # entier très grand
    entier = models.IntegerField()          # entier standard
    petit_entier = models.SmallIntegerField() # petit entier
    decimal = models.DecimalField(max_digits=10, decimal_places=2) # Nombre decimal avec precision
    flottant = models.FloatField()          # Nombre à virgule flottante
    positif = models.PositiveIntegerField() # Entier positif
    positif_petit = models.PositiveSmallIntegerField() # petit entier positif
    
    # Champs booléens
    est_actif = models.BooleanField(default=True) # True/False
    est_visible = models.BooleanField(null=True, blank=True) # True/False ou Null
    
    #champs texte
    nom = models.CharField(max_length=100) # court texte
    description = models.TextField()       # long texte
    slug = models.SlugField()              # Texte court utilisable dans une url
    email = models.EmailField()            # email valide
    url = models.URLField()                # url valide
    
    # Champs date et heure 
    date_naissance = models.DateField()  # Date uniquement
    heure = models.TimeField()           # Heure uniquement
    date_heure = models.DateTimeField()  # Date + heure
    duree = models.DurationField()       # durée
    
    # champs binaires
    dichier = models.FileField(upload_to='uploads/')  # Fichier
    image = models.ImageField(upload_to='images/')    # Image
    binaire = models.BinaryField()                    # Données binaires brutes
    
    # champs de relations
    
parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True) # Relation a soi meme
groupe = models.ManyToManyField('self', symmetrical=False)                          # plusieurs relations
profil = models.OneToOneField('Profil', on_delete=models.CASCADE)                   # Relation 1 - 1

