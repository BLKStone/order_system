
from django.db import models

# Create your models here.

class Employee(models.Model):
    name =  models.CharField(max_length = 20)
    password = models.CharField(max_length = 10) 
    emp_type = models.IntegerField()

    def __unicode__(self):
        return self.name



class Order(models.Model):
    id = models.AutoField( primary_key = True )
    time = models.DateTimeField('date published')
    desk_id = models.IntegerField()
    total_price = models.FloatField()
    state = models.IntegerField()
    employee = models.ForeignKey(Employee)

    def __unicode__(self):
        return str(self.id)


class Tea(models.Model):
    name = models.CharField(max_length = 20)
    price = models.FloatField()

    def __unicode__(self):
        return self.name

class Order_Tea(models.Model):
    order = models.ForeignKey(Order)
    tea = models.ForeignKey(Tea)
    number = models.IntegerField()

    def __unicode__(self):
        return str(self.order_id)+','+str(self.tea_id)



