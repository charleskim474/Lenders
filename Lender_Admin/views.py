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
        uname = request.POST.get('uname')
        pw = request.POST.get('pw')
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
                return redirect('app:home')
        else:
            return render(request, 'index.html', {'msg':'Invalid Username or Password, please try again!'})
    return render(request, 'index.html')


def home(request):
    access = request.session.get('uname', 'deny')
    if access != 'deny':
        row = Lender.objects.get(username = access)
        return render(request, 'dashboard.html', {'lender' : row})
    else:
        return redirect('app:login')


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
            
                name = request.POST.get('name')
                tel = request.POST.get('tel')
                email = request.POST.get('email')
                location = request.POST.get('location')
                NIN = request.POST.get('NIN')
                try:
                    NINcheck = Borrower.objects.get(lender_id = lender, NIN = NIN)
                    if NINcheck.NIN == NIN:
                        print('===>>Identical NIN found')
                        return render(request, 'new_borrower.html', {'NINerr':'NIN already used In this Company!'})
                except Borrower.DoesNotExist:
                    print('===>>No Identical NIN found')
                pin = request.POST['pin']
                photo = request.FILES['photo']
                Borrower.objects.create(
                    lender_id = lender,
                    name = name,
                    tel = tel,
                    email = email,
                    location = location,
                    NIN = NIN,
                    pin = pin,
                    photo = photo
                )
                print('\n\n===>added borrower\n\n', name)
                borrower = Borrower.objects.get(lender_id = lender, NIN = NIN)
                
                #ADD A  LOAN FOR THE BORROWER
                
                loan_amount = request.POST.get('loan_amount')
                interest_rate = request.POST.get('interest_rate')
                processing_fee = request.POST.get('processing_fee')
                duration = request.POST.get('duration')
         ##########       
                last_date = date.today() + timedelta(days = int(duration))
                total_amm = int(loan_amount) + int(processing_fee) + ( (float(interest_rate)/100) * int(loan_amount))
         ############       
                Loans.objects.create(
                    lender_id = lender,
                    borrower_id = borrower,
                    loan_amount = loan_amount,
                    interest_rate = interest_rate,
                    processing_fee = processing_fee,
                    total_amm = total_amm,
                    duration = duration,
                    last_date = last_date,
                    balance = total_amm
                )
                print('\n\n===>added loan for\n\n', name)
                loan = Loans.objects.get(lender_id = lender, borrower_id = borrower)
                
         #ADDING AN Aggreement TO A LOAN
         
                aggreement = request.FILES.get('aggreement')
         ############
                Aggreements.objects.create(
                    lender_id = lender,
                    borrower_id = borrower,
                    loan_id = loan,
                    aggreement = aggreement
                )
                print('\n\n===>added agreement for\n\n', name)
                aggreement = Aggreements.objects.get(lender_id = lender, borrower_id = borrower)
                
         #ADDING COLLATERAL INFO
                
                asset_name = request.POST.get('asset_name')
                description = request.POST.get('description')
                proof = request.FILES.get('proof')
                asset_photo = request.FILES.get('asset_photo')
        #############        
                Collateral.objects.create(
                    lender_id = lender,
                    borrower_id = borrower,
                    loan_id = loan,
                    aggr_id = aggreement,
                    asset_name = asset_name,
                    description = description,
                    proof = proof,
                    asset_photo = asset_photo
                )
                print('\n\n===>added Collateral info for\n\n', name)
                return redirect('app:loans')
                #return redirect('app:dashboard')
            except Exception:
                try:
                    Borrower.objects.get(lender_id = lender, NIN = NIN).delete()
                    print('\n\n===>Borrower info deleted \n\n', name)
                except Borrower.DoesNotExist:
                    print('\n\n===>error \n\n', name)
                return render(request, 'new_borrower.html', {'msg': 'Error occured during form handling!, check for errors & save again. '})
                #return ErrorPage
        return render(request, 'new_borrower.html')
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
            today = date.today()
           # today = today.days
            return render(request, 'customers.html', {'loan':loan, 'today': today })
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
                borrower_id = request.POST.get('id')
                paid = request.POST.get('paid')
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
                    #return error page
            return render(request, 'index.html', {'msg':'Invalid Username or Password, please try again!'})
        except Borrower.DoesNotExist:
            return render(request, 'index.html', {'msg':'Invalid Username or Password, please try again!'})