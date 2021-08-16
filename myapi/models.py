
# Create your models here.
from django.db import models

# Create your models here.
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.firstname), filename])

class userinfo(models.Model):
    gamename=models.CharField(max_length=15)
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    elorating=models.IntegerField()
    tournamentsplayed=models.IntegerField()
    tournamentswon=models.IntegerField()
    winpercent=models.IntegerField()
    
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    
    

    def __str__(self):
        return self.firstname