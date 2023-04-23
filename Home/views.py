from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.
def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        desc = request.POST.get('message')
        contact = Contact(email=email, desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'home.html')