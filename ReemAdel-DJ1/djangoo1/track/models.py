from django.db import models

# Create your models here.
class Track(models.Model):
    id=models.AutoField(primary_key=True)
    first_track_name=models.CharField(max_length=60,null=False)
    first_track_image=models.ImageField(upload_to='track1/images/')
    second_track_name=models.CharField(max_length=60,null=False)
    second_track_image=models.ImageField(upload_to='track2/images/')
    status=models.BooleanField(default=True)
    
    @classmethod
    def getalltracks(cls):
        return cls.objects.all()
    
    @classmethod
    def gettrackbyid(cls,id):
        return cls.objects.get(id=id)


