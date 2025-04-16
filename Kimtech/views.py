#Kimtech Views

from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import HttpResponse
from .models import *
from .logic import exp_check

# Create your views here.


def index(request):
    #Login logic here.
    return render(request, 'index.html')

#VIEW AVAILABLE LENDERS
def lenders(request):
    exp_check()
    lender = Lender.objects.all()
    return render(request, 'lenders.html', {'lender':lender})
    
    
#OPEN/ Create lender account
def create_account(request):
    exp_check()
    if request.method == 'POST':
        co_name = request.POST['co_name']
        tel = request.POST['tel']
        email = request.POST['email']
        username = request.POST['uname']
        password = request.POST['pw']
        location = request.POST['location']
        try:
            Lender.objects.create(
                co_name = co_name, 
                tel = tel, email = email, 
                username =username, 
                password = password, 
                location = location, 
                subscription = True,
                subscription_status = 'Trial'
             )#Expiry is added automatically
            print('\n\n=====>>SAVED lender SUCCESSFULLY\n\n')
            return HttpResponse('<h1>Created</h1>')
        except IntegrityError as e:
            print('===>Exception : ', e)
            lender = Lender.objects.all()
            return render(request, 'lenders.html', {'lender':lender, 'ex':e, 'uname':username })#
    lender = Lender.objects.all()#
    return render(request, 'lenders.html', {'lender':lender})#