from django.contrib import admin

from ordersys.models import  Employee
from ordersys.models import  Order
from ordersys.models import  Tea
from ordersys.models import  Order_Tea

# Register your models here.
admin.site.register(Employee)
admin.site.register(Tea)
admin.site.register(Order)
admin.site.register(Order_Tea)
