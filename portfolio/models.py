from django.db import models

class Project(models.Model):
    #https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ImageField - tyt dani pro field's
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="portfolio/images/")
    url=models.URLField(blank='True')
def __str__(self):
    return self.title
