from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
 
class patient(models.Model):
     id = models.AutoFields(primary_key=True)
     nom = models.CharField(max_length=50)
     prenom = models.CharField(max_length=50)
     user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="consultation" )
     email = models.EmailField(max_lenght=40)
     telephone = models.PositiveIntegerField()
     age = models.PositiveIntegerField()
     statut_civil = models.CharField(max_length=40)
     genre = models.CharField(max_length=6)
     
class consultation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    patient = models.ForeignKey(patient, on_delete= models.CASCADE, related_name="consultations")
      



    def clean(self):
        if self.heure_fin <= self.heure_debut:
            raise ValidationError("L'heure de fin doit être après l'heure de début.")

        chevauchement = consultation.objects.filter(
            patient=self.patient,
            date=self.date,
            heure_debut__lt=self.heure_fin,
            heure_fin__gt=self.heure_debut
        ).exclude(pk=self.pk)

        if chevauchement.exists():
            raise ValidationError("Ce patient a déjà un autre rendez-vous.")  
    
    
         
     
     
       