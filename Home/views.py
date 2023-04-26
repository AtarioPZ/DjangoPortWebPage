from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.http import FileResponse, Http404

# Create your views here.
def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        desc = request.POST.get('message')
        contact = Contact(email=email, desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'home.html')

def gameprojects(request):
    return render(request, 'gameprojects.html')

def appprojects(request):
    return render(request, 'appprojects.html')

def cv(request):
    with open('/static/files/test.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=test.pdf'
        return response
    pdf.closed