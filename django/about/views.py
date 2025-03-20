from django.shortcuts import render,HttpResponse
from .models import MyInformation, SocialMedia

# Create your views here.
def index(request):
    aboutme = MyInformation.objects.first()
    socials = SocialMedia.objects.all()

    data = {
        "name": f"{aboutme.first_name} {aboutme.last_name}",
        "bio" : aboutme.bio,
        "social" : socials,
        "photo" : aboutme.photo.url,
    }
    return render(request=request,template_name="index.html",context=data)