#Lenders Admin Views
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Kimtech.models import *
from datetime import date, timedelta
from Kimtech.logic import exp_check

# Create your views here.
#LOGIN FOR LENDER
def login(request):
    exp_check()
    if request.method == 'POST':
        uname = request.POST['uname']
        pw = request.POST['pw']
        try:
            row = Lender.objects.get(username = uname)
        except Lender.DoesNotExist as e:
            request.session['uname'] = uname
            request.session['pw'] = pw
            return redirect('app:status')
        if row and row.password == pw:
            request.session['uname'] = uname
            print(f"===Added : {request.session.get('uname', 'Sessiom Not Added')} to session")
            
            if row.subscription == False:
                return render(request, 'index.html', {'msg':'Hello customer, your subscription expired, please subscribe and gain access!'})
            else:
                return redirect('app:add_borrower')
            #return Dashbord
        else:
            return render(request, 'index.html', {'msg':'Invalid Username or Password, please try again!'})
    return render(request, 'index.html')


#Logout FOR ALL
def logout(request):
    exp_check()
    request.session.flush()
    return redirect('app:login')



#REGISTER BORROWERS & all loan info
def add_borrower(request):
    exp_check()
    access = request.session.get('uname', 'deny')
    if access != 'deny':
        print('===>Loged in with ',access)
        if request.method == 'POST':
            try:
                lender = Lender.objects.get(username = access)
                
            #ADDING BORROWER
                """name = request.POST['name']
                tel = request.POST['tel']
                email = request.POST['email']
                location = request.POST['location']
                NIN = request.POST['NIN']
                pin = request.POST['pin']
                photo = request.FILE['photo']
                Borrower.objects.create(
                    lender_id = lender
                    name = name
                    tel = tel
                    email = email
                    location = location
                    NIN = NIN
                    pin = pin
                    photo = photo
                )
                print('===>added borrower', name)
                #ADD A  LOAN FOR THE BORROWER
                lender_id
                brorrower_id
                loan_amount = request.POST[
                interest_rate = request.POST[
                processing_fee = request.POST[
                total_amm
                duration = request.POST[
                last_date
                balance
                
                #Aggreements
                lender_id 
                borrower_id
                loan_id 
                loan_date#AUTO
                aggreement = request.FILE[
                
                
                #COLLATERAL INFO
                lender_id 
                borrower_id 
                loan_id 
                aggr_id 
                asset_name = request.POST[
                description = request.POST[
                proof = request.FILE[
                asset_photo = request.FILE["""
                return HttpResponse('<h1>Under implementation wait!')
            except Exception:
                return HttpResponse('Error!')
        return HttpResponse('<h1>Request Method isnt POSTUnder implementation wait!, but')
    return redirect('app:login')




#VIEW BORROWERS (Lender based after login) WITH ALL LOANS
def customers(request):
    exp_check()
    access = request.session.get('uname', 'deny')
    if access != 'deny':
        lender = Lender.objects.get(username = access)
        if lender.subscription == False:
            return render(request, 'index.html', {'msg':'Hello customer, your subscription expired, please subscribe and gain access!'})
        else:
            lender_id = lender.id
            loan = Loans.objects.filter(lender_id = lender_id)
            print('===>', access)#....
            return render(request, 'customers.html', {'loan':loan})
    return redirect('app:login')


#RETURNS ALL LOANS OF A LENDER
def loans(request):
    exp_check()
    access = request.session.get('uname', 'deny')
    if access != 'deny':
        lender = Lender.objects.get(username = access)
        if lender.subscription == False:
            return render(request, 'index.html', {'msg':'Hello customer, your subscription expired, please subscribe and gain access!'})
        else:
            lender_id = lender.id
            loans = Loans.objects.filter(lender_id = lender_id)
            print('===>', access)#...
            today = date.today()
            return render(request,'loans.html', {'loans': loans, 'today':today})
    return redirect('app:login')



#Repayments RECORDS REPAYMENTS & RETURNS THE REPAYMENTS LIST
def repayments(request):
    exp_check()
    access = request.session.get('uname', 'deny')
    if access != 'deny':
        lender = Lender.objects.get(username = access)
        if lender.subscription == False:
            return render(request, 'index.html', {'msg':'Hello customer, your subscription expired, please subscribe and gain access!'})
        else:
            if request.method == 'POST':
            #select name from drop down list
                borrower_id = request.POST['id']
                paid = request.POST['paid']
                borrower = Borrower.objects.get(id = borrower_id, lender_id = lender)
                loan = Loans.objects.get(lender_id = lender, borrower_id = borrower)
                loan.total_amm
                bal = loan.balance - int(paid)
                percentage_paid = 100 - ( ( bal/loan.total_amm ) * 100 )
                time_left = loan.last_date - date.today()
                Repayment.objects.create(
                    lender_id = lender,
                    borrower_id = borrower,
                    loan_id = loan,
                    paid = paid,
                    percentage_paid = percentage_paid,
                    time_left = time_left.days,
                    bal = bal
                )
                print('====> Repayment added for ', loan.borrower_id.name)
                Loans.objects.filter(lender_id=lender, borrower_id=borrower).update(balance=bal)
                repayments = Repayment.objects.filter(lender_id = lender)
                loans = Loans.objects.filter(lender_id = lender)
                return render(request, 'repayments.html',{'repayments': repayments, 'pay':'pay', 'loans':loans})
            repayments = Repayment.objects.filter(lender_id = lender)
            loans = Loans.objects.filter(lender_id = lender)
            return render(request, 'repayments.html',{'repayments': repayments, 'pay':'pay', 'loans':loans})# loans provide drop down list
    return redirect('app:login')
    
#Aggreements & collateral information
def aggreements(request):
    exp_check()
    access = request.session.get('uname', 'deny')
    if access != 'deny':
        lender = Lender.objects.get(username = access)
        if lender.subscription == False:
            return render(request, 'index.html', {'msg':'Hello customer, your subscription expired, please subscribe and gain access!'})
        else:
            #use collateral model to get all required information
            collateral = Collateral.objects.filter(lender_id = lender)
            return render(request, 'aggreements.html', {'info': collateral})
    return redirect('app:login')


#Borrower access
def status(request):
        user = request.session.get('uname')
        password = request.session.get('pw')
        try:
            customer = Borrower.objects.get(NIN = user, pin = password)
            if customer.NIN == user and customer.pin == password:
                print('===>>>Customer added to session ', customer.name)
                try:
                    data = Collateral.objects.get(lender_id = customer.lender_id, borrower_id = customer)
                    repayments = Repayment.objects.filter(lender_id = customer.lender_id, borrower_id = customer)
                    return render(request, 'info.html', {'data':data, 'info':repayments})
                except Exception:
                    print('===>No collateral info found')
                    return HttpResponse('<h1>Missing Information In The System, Please Contact your Lender For Assistance! <br />Thank you.</h1>')
            return render(request, 'index.html', {'msg':'Invalid Username or Password, please try again!'})
        except Borrower.DoesNotExist:
            return render(request, 'index.html', {'msg':'Invalid Username or Password, please try again!'})