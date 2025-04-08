from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Lender)
admin.site.register(Borrower)
admin.site.register(Loans)
admin.site.register(Repayment)
admin.site.register(Aggreements)
admin.site.register(Collateral)