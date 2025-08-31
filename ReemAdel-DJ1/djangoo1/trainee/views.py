from django.http import HttpResponseRedirect
from django.shortcuts import render
from track.models import Track
from .models import Trainee

# Create your views here.
def alltrainee(request):
    context={}
    context['trainees']=Trainee.getalltrainee()
    return render(request,'trainee/trainee.html',context)
def insert(request):
    if request.method=="POST":
        Trainee.objects.create(name=request.POST['name'],email=request.POST['email'],track=request.POST['track'],img=request.FILES['img'],trackid=Track.gettrackbyid(request.POST['trackid']))
    return render(request,'trainee/insert.html',{'tracks':Track.getalltracks()})

def update(request,id):
    trainee=Trainee.gettraineebyid(id)
    context={'trainee':trainee}
    context['tracks']=Track.getalltracks()
    if request.method=="POST":
        trainee.name=request.POST['name']
        trainee.email=request.POST['email']
        trainee.track=request.POST['track']
        trainee.trackid=Track.gettrackbyid(request.POST['trackid'])
        if request.FILES.get('img'):
            trainee.img=request.FILES['img']
        trainee.save()
        return HttpResponseRedirect('/Trainee/')
    return render(request,'trainee/update.html',context)

def delete(request,id):
    Trainee.objects.filter(id=id).update(status=False)
    return HttpResponseRedirect('/Trainee/')