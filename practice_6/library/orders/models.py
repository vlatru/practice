from django.db import models
from library.models import *
from datetime import datetime
from utils.models import TimeStampedModel
# Create your models here.


class Customer(TimeStampedModel):
    firstName = models.CharField('Name', max_length=32)
    lastName = models.CharField('Surname', max_length=32)
    address = models.TextField('Address')
    is_approved = models.BooleanField()
    email = models.EmailField('Email')

    def __unicode__(self):
        return u'%s %s' % (
            self.lastName, self.firstName)


class Order(TimeStampedModel):
    itemId = models.ForeignKey(Book)
    create = models.DateField('Order Date', default=datetime.now)
    customer = models.ForeignKey(Customer, null=True)
