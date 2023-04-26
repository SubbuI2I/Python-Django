from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.name} ({self.address})'
    
class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f'{self.email}'
    
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)    
    email = models.ManyToManyField(Participant, blank=True, null=True)
    organizeremail = models.EmailField()
    date = models.DateField()
    
    def __self__(self):
        return f"{self.title} - {self.slug}"

