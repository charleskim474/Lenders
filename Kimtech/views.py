from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    lender = Lender.objects.all()
    return render(request, 'index.html', {'lender':lender})
    
    
#OPEN lender account
def create_account(request):
    if request.method == 'POST':
        co_name = request.POST['co_name']
        tel = request.POST['tel']
        email = request.POST['email']
        username = request.POST['uname']
        password = request.POST['pw']
        location = request.POST['location']
        #subscription logic here
        #Expiry check & update here
        Lender.objects.create(co_name = co_name, tel = tel, email = email, username =username, password = password, location = location, expiry = '2025-04-03')
        print('\n\n=====>>SAVED SUCCESSFULLY\n\n')
        
      #  lender = Lender.objects.all()
        #return redirect('/index/')
        return HttpResponse('<h1>Created</h1>')
#    lender = Lender.objects.all()
   # return render(request, 'index.html', {'lender':lender})