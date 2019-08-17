from django.contrib import messages
from django.shortcuts import render
from .models import carousel

def index(request):
    context=dict()
    context['images']=carousel.objects.filter(status="published")
    # context['images']=images
    return render(request, 'home/index.html', context)

# stuff not checke
def carousel_create(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        carousel = carousel.objects.create(title=request.POST.get('title'))
        messages.success(request, 'something is added successfully')
    return render(request, 'manage/carousel_create.html', {})

