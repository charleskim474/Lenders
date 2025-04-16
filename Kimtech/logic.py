#Logic In Kimtech
from .models import Lender, Loans, Repayment
from datetime import date, timedelta

#SUBSCRIPTIONS

#Check status
def exp_check():
    lender_check = Lender.objects.all()
    for l in lender_check:
        exp = l.expiry
        if exp >= date.today():
            Lender.objects.filter(id = l.id).update(subscription = True) #
            t_left = exp - date.today()#
            Lender.objects.filter(id = l.id).update(time_left = t_left.days)#
        else:
            Lender.objects.filter(id = l.id).update(subscription = False)#
            Lender.objects.filter(id = l.id).update(subscription_status = 'Working')#
            Lender.objects.filter(id = l.id).update(time_left = -1)###
    loan = Loans.objects.all()
    for l in loan:
        time_left = l.last_date - date.today()
        Repayment.objects.filter(loan_id = l.id).update(time_left = time_left.days)