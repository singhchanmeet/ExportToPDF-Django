from django.shortcuts import render
from .models import MyForm

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        photograph = request.FILES['photograph']
        newform = MyForm(name=name, email=email, phone_number=phone_number, photograph=photograph)
        newform.save()
    return render(request,'index.html')
