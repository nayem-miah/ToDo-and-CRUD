from django.db import models

class Form1(models.Model):
    name = models.CharField('your Name', max_length=40)
    email = models.EmailField('Your Email')
    zip_code= models.CharField('Your Zip Code', max_length=30)
    phone = models.CharField('Your Phone', max_length=30)
    website = models.URLField('Website Link')

    def __str__(self):
        return self.name
