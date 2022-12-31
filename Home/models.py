from django.db import models

class ServiceModel (models.Model):
    ServiceImage=models.ImageField(upload_to= "Serviceimage/",null=True)
    ServiceTitle=models.CharField(max_length=70,null=True)
    ServiceDescrption=models.CharField(max_length=400,null=True)


