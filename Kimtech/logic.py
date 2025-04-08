from .models import Lender

#SUBSCRIPTIONS
class Subscription:
    def __init__(self, co_id, status):
        self.co_id = co_id
        self.status = status
     
     #Check status
     def status_check(self, co_id):
         self.status = Lender.objects.get(id = co_id).values('subscription')
         return self.status
         
     #Update suscription status
     def update_status():
         pass
         
     #Update initial expiry date