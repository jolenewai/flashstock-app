from django.db import models
from customers.models import Customer
from photographers.models import Photographer


# Create your models here.


class Request(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    request_to = models.ForeignKey(
        Photographer,
        on_delete='CASCADE',
        related_name='request_to'
    )
    request_from = models.ForeignKey(
        Customer,
        on_delete='CASCASE',
        related_name='request_from'
    )

    def __str__(self):
        return '#' + str(self.id) + ' - ' + self.title
