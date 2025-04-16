#General models (Kimtech)

from django.db import models
from datetime import date, timedelta

#Lenders' information

class Lender(models.Model):
    co_name = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 13)
    email = models.EmailField()
    username = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    subscription = models.BooleanField(default = False)
    expiry = models.DateField(default = date.today() + timedelta(days = 30)) #Automatically add 30days expiry from today
    subscription_status = models.CharField(max_length = 10, default = 'Trial') #Trial/Working
    time_left = models.IntegerField(default = -1)
    
    
#Borrower information

class Borrower(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    tel = models.CharField(max_length = 13)
    email = models.EmailField()
    location = models.CharField(max_length = 100)
    NIN = models.CharField(max_length = 20)
    pin = models.CharField(max_length = 10)
    photo = models.ImageField(upload_to = 'images/')
    
#Loans information

class Loans(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE)
    borrower_id = models.ForeignKey(Borrower, on_delete = models.CASCADE)
    loan_Date = models.DateField(auto_now_add = True)
    loan_amount = models.IntegerField()
    interest_rate = models.DecimalField(max_digits = 5, decimal_places = 3)
    processing_fee = models.IntegerField()
    total_amm = models.DecimalField(max_digits = 9, decimal_places = 3)
    duration = models.IntegerField()
    last_date = models.DateField()
    balance = models.DecimalField(max_digits = 20, decimal_places = 3)
    
    
#Aggreement
class Aggreements(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE, null = True)
    borrower_id = models.ForeignKey(Borrower, on_delete = models.CASCADE, null = True)
    loan_id = models.ForeignKey(Loans, on_delete = models.CASCADE, null = True)
    loan_date = models.DateField(auto_now_add = True)
    aggreement = models.ImageField(upload_to = 'images/', null = True)
    
    
#Collateral info

class Collateral(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE, null = True)
    borrower_id = models.ForeignKey(Borrower, on_delete = models.CASCADE, null = True)
    loan_id = models.ForeignKey(Loans, on_delete = models.CASCADE, null = True)
    aggr_id = models.ForeignKey(Aggreements, on_delete = models.CASCADE, null = True)
    asset_name = models.CharField(max_length = 100, default = 'Not Added')
    description = models.TextField(default = 'Not Added')
    proof = models.ImageField(upload_to = 'images/', null = True)
    asset_photo = models.ImageField(upload_to = 'images/', null = True)
    

#REPAYMENT

class Repayment(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE, null = True)
    borrower_id = models.ForeignKey(Borrower, on_delete = models.CASCADE, null = True)
    loan_id = models.ForeignKey(Loans, on_delete = models.CASCADE, null = True)
    date = models.DateField(auto_now_add = True)
    paid = models.IntegerField(default = 0)
    bal = models.DecimalField(max_digits = 9, decimal_places = 3)
    percentage_paid = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    time_left = models.IntegerField()