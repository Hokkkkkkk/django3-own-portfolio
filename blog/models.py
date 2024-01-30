from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=False)
    description=models.CharField(max_length=999)
    url=models.URLField(blank='True')
