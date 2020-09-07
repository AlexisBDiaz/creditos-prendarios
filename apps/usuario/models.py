from django.db import models

class User(models.Model):
    name        = models.CharField( max_length=50, blank=True )
    phone       = models.IntegerField( null=False )
    address     = models.CharField( max_length=50, blank=True ) 
    business    = models.IntegerField( null=False ) #Empresa en la que elabora
    antiquity   = models.IntegerField( null=False ) #Tiempo de laborar en la empresa
    loan        = models.IntegerField( null=False ) #Monto autorizado del credito
  

    class Meta:
        db_table = "user"
