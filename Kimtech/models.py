from django.db import models

#Lenders' information

class Lender(models.Model):
    co_name = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 13)
    email = models.EmailField()
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    subscription = models.BooleanField(default = False)
    expiry = models.DateField()
    
    
#Borrower information

class Borrower(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    tel = models.CharField(max_length = 13)
    email = models.EmailField()
    location = models.CharField(max_length = 100)
    NIN = models.CharField(max_length = 20)
    pin = models.CharField(max_length = 10)
    photo = models.ImageField()
    
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
    
#REPAYMENT

class Repayment(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE)
    borrower_id = models.ForeignKey(Borrower, on_delete = models.CASCADE)
    loan_id = models.ForeignKey(Loans, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    paid = models.IntegerField()
    bal = models.DecimalField(max_digits = 9, decimal_places = 3)
    percentage_paid = models.DecimalField(max_digits = 5, decimal_places = 3)
    time_left = models.IntegerField()
    
#Aggreement
class Aggreements(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE)
    borrower_id = models.ForeignKey(Borrower, on_delete = models.CASCADE)
    loan_id = models.ForeignKey(Loans, on_delete = models.CASCADE)
    loan_date = models.DateField(auto_now_add = True)
    aggreement = models.ImageField()
    
    
#Vollayeral info

class Collateral(models.Model):
    lender_id = models.ForeignKey(Lender, on_delete = models.CASCADE)
    borrower_id = models.ForeignKey(Borrower, on_delete = models.CASCADE)
    loan_id = models.ForeignKey(Loans, on_delete = models.CASCADE)
    aggr_id = models.ForeignKey(Aggreements, on_delete = models.CASCADE)
    asset_name = models.CharField(max_length = 100)
    description = models.TextField()
    proof = models.ImageField()
    asset_photo = models.ImageField()