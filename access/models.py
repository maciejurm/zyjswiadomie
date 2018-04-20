from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import getpaid

class Order(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currency = models.CharField(max_length=3, default='PLN')
    status = models.CharField(max_length=1, blank=True, default='W', choices=(('W', 'Waiting for payment'),
                                                                               ('P', 'Payment complete')))
    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

Payment = getpaid.register_to_payment(Order, unique=False, related_name='payments')