from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Image

# Create your views here.
def home(request):
    return render(request, "home.html", {'Choose':'Choose'})

def bar(request):
    bar_images = Image.objects.filter(image_type='bar')
    return render(request, 'bar.html', {'bar': bar_images, 'Choose':'BAR'})

def cone(request):
    cone_images = Image.objects.filter(image_type='cone')
    return render(request, "cone.html",{'cone': cone_images, 'Choose':'CONE'})

def sundae(request):
    sundae_images = Image.objects.filter(image_type='sundae')
    return render(request, "sundae.html",{'sundae': sundae_images, 'Choose':'SUNDAE'})

def cake(request):
    cake_images = Image.objects.filter(image_type='cake')
    return render(request, "cake.html",{'cake': cake_images, 'Choose':'CAKE'})

def list(request):
    list_images = Image.objects.filter(list=True)
    return render(request, "list.html",{'list': list_images, 'Choose':'LIST'})

# for list
@csrf_exempt
def toggle_list(request, image_id):
    if request.method == 'POST':
        image = Image.objects.get(id=image_id)
        image.list = not image.list
        image.save()
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'}, status=400)