from django.db import models
from track.models import Track

# Create your models here.
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=60)
    track=models.CharField(max_length=30)
    img=models.ImageField(upload_to='trainee/images')
    status=models.BooleanField(default=True)
    trackid=models.ForeignKey(Track,on_delete=models.CASCADE)
    
    @classmethod
    def getalltrainee(cls):
        return cls.objects.all()
    
    @classmethod
    def gettraineebyid(cls,id):
        return cls.objects.get(id=id)