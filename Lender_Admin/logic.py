from Kimtech.models import *

class Statistics:
    def getTotalLoans(self, lender_id):
        loans = Loans.objects.filter(lender_id = lender_id)
        total = 0
        for l in loans:
            total = total+1
        return total
        
        
    def totalLoanAmount(self, lender_id):
        loans = Loans.objects.filter(lender_id = lender_id)
        total_amm = 0
        for l in loans:
            total_amm = total_amm + l.total_amm
        return total_amm
        
        
    def ptPaid(self, lender_id):
        paid = 0
        loans = Loans.objects.filter(lender_id = lender_id)
        for l in loans:
            paid += (l.total_amm - l.balance)
        try:
            paid_rate = (paid/self.totalLoanAmount(lender_id)) * 100
        except ZeroDivisionError:
            paid_rate = 0
        return [paid, paid_rate]
        
        
    def fullPay(self, lender_id):
        loans = Loans.objects.filter(lender_id = lender_id)
        fully = 0
        count = 0
        for l in loans:
            if l.balance <= 0:
                count += 1
                fully += l.total_amm
        try:
            rate = (fully/self.totalLoanAmount(lender_id)) * 100
        except ZeroDivisionError:
            rate = 0
        return [count, rate, fully]
        
        
    def unpaid(self, lender_id):
        loans = Loans.objects.filter(lender_id = lender_id)
        bal = 0
        rate = 0
        for l in loans:
            bal += l.balance
        try:
            rate = (bal/self.totalLoanAmount(lender_id)) * 100
        except ZeroDivisionError:
            rate = 0
        return [bal, rate]
        
        
    def interest(self, lender_id):
        loans = Loans.objects.filter(lender_id = lender_id)
        paid_so_far = 0
        interest = 0
        exp_intr = 0
        for l in loans:
            exp_intr += l.total_amm - l.loan_amount
            paid_so_far = l.total_amm - l.balance
            if paid_so_far >= l.loan_amount:
                interest += (paid_so_far - l.loan_amount)
        try:
            rate = (interest/exp_intr) * 100
        except ZeroDivisionError:
            rate = 0
        return [exp_intr, interest, rate]