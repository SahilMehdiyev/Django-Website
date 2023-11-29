from django.db import models


class Feature(models.Model):
    name    = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    

class Content(models.Model):
    header  = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    text    = models.CharField(max_length=400)
    # img = models.ImageField()
    
    def __str__(self):
        return self.header
        
        
# class Project(models.Model):
#     header = models.CharField(max_length=100)
#     detail = models.CharField(max_length=200)
    
class Card(models.Model):
    title   = models.CharField(max_length=100)
    detail  = models.CharField(max_length=200)
    url     = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title


class Values(models.Model):
    title   = models.CharField(max_length=100)
    detail  = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title   = models.CharField(max_length=100)
    detail  = models.CharField(max_length=200)
    # url     = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
    
class Design(models.Model):
    title    = models.CharField(max_length=100)
    text     = models.CharField(max_length=400)
    img      = models.ImageField(upload_to = 'images/',blank=True)
    url      = models.TextField(max_length=100)
    ictenImg = models.ImageField(upload_to = 'images/',blank=True)
    
    
    def __str__(self):
        return self.title
    
class Kartlar(models.Model):
    title   = models.CharField(max_length=100)
    text    = models.CharField(max_length=400)
    img     = models.ImageField(upload_to = 'images/')
    
    def __str__(self):
        return self.title
    
      
    
    

   
        
    
    
    
        
        
        
    
    
            
    
