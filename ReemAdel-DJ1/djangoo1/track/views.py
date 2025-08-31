from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.models import Track

# Create your views here.
def alltracks(Requist):
    context={}
    context['tracks']=Track.objects.all()
    return render(Requist,'track/index.html',context)

def update(request,id):
    track=Track.objects.get(id=id)
    context={'track':track}
    if request.method == "POST":
      track.first_track_name=request.POST['track_name_1st']
      if request.FILES.get('track_img_1st'):
        track.first_track_image=request.FILES['track_img_1st']
      track.second_track_name=request.POST['track_name_2nd']
      if request.FILES.get('track_img_2nd'):
        track.second_track_image=request.FILES['track_img_2nd']
      track.save()
      return HttpResponseRedirect('/Track/')

    return render(request,'track/update.html',context)

def insert(request):
    if request.method == "POST":
      track_name1=request.POST['track_name_1st']
      track_img1=request.FILES['track_img_1st']
      track_name2=request.POST['track_name_2nd']
      track_img2=request.FILES['track_img_2nd']
      Track.objects.create(first_track_name=track_name1,first_track_image=track_img1,second_track_name=track_name2,second_track_image=track_img2)
    return render(request,'track/insert.html')

def delete(Requist,id):
    Track.objects.filter(id=id).update(status=False)
    return HttpResponseRedirect('/Track/')
