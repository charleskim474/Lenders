from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('login', views.login, name = 'login'),
    path('add_borrower', views.add_borrower, name = 'add_borrower'),
    path('customers', views.customers, name = 'customers'),
    path('loans', views.loans, name = 'loans'),
    path('repayments', views.repayments, name = 'repayments'),
    path('logout', views.logout, name = 'logout'),
    path('aggreements', views.aggreements, name = 'aggreements'),
    path('status', views.status, name = 'status')
]