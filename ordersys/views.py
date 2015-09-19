from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt 

from django.utils import timezone

from datetime import datetime
from datetime import timedelta

from .models import Employee
from .models import Order
from .models import Tea
from .models import Order_Tea

import sqlite3

# Create your views here.

@csrf_exempt 
def mainpage(request):
    return render(request,'mainpage2.html',{})

@csrf_exempt 
def about(request):
    return render(request,'about.html',{})

@csrf_exempt 
def order(request):
    tea_list = Tea.objects.all()
    emp_list = Employee.objects.all()
    return render(request,'order.html',{'tea_list':tea_list,'emp_list':emp_list})

@csrf_exempt
def unfinorder(request):
    order_list = Order.objects.filter( state = 0 ).order_by('-time')
    raw_sql = 'SELECT * FROM ordersys_order_tea WHERE order_id IN (SELECT id FROM ordersys_order WHERE state = 0 )'
    order_tea_list = Order_Tea.objects.raw(raw_sql)
    return render(request,'unfinoder.html',{ 'order_list':order_list,'order_tea_list':order_tea_list})

@csrf_exempt
def endorder(request):
    order_id = request.POST.get('order_id','99999999')
    change_order = Order.objects.get(pk = order_id)
    change_order.state = 1
    change_order.save()

    order_list = Order.objects.filter( state = 0 ).order_by('-time')
    raw_sql = 'SELECT * FROM ordersys_order_tea WHERE order_id IN (SELECT id FROM ordersys_order WHERE state = 0 )'
    order_tea_list = Order_Tea.objects.raw(raw_sql)
    return render(request,'unfinoder.html',{ 'order_list':order_list,'order_tea_list':order_tea_list})

@csrf_exempt
def delorder(request):
    order_id = request.POST.get('order_id2','99999999')
    change_order = Order.objects.get(pk = order_id)
    change_order.delete()

    order_list = Order.objects.filter( state = 0 ).order_by('-time')
    raw_sql = 'SELECT * FROM ordersys_order_tea WHERE order_id IN (SELECT id FROM ordersys_order WHERE state = 0 )'
    order_tea_list = Order_Tea.objects.raw(raw_sql)
    return render(request,'unfinoder.html',{ 'order_list':order_list,'order_tea_list':order_tea_list})

@csrf_exempt
def finorder(request):
    order_list = Order.objects.filter( state = 1 ).order_by('-time')[:5]
    raw_sql = 'SELECT * FROM ordersys_order_tea WHERE order_id IN (SELECT id FROM ordersys_order WHERE state = 1 )'
    order_tea_list = Order_Tea.objects.raw(raw_sql)
    return render(request,'finorder.html',{ 'order_list':order_list,'order_tea_list':order_tea_list })

@csrf_exempt
def stat(request):
    #order_list = Order.objects.filter( state = 1, time =  ).order_by('-time')

    cx = sqlite3.connect("/home/ray/dev/django/order_system/db.sqlite3")
    cu = cx.cursor()

    time = timezone.now().strftime('%Y-%m-%d')
    #print time 

    raw_sql_front = '''
    select ordersys_tea.id,ordersys_tea.name,sum(number) from ordersys_order,ordersys_order_tea,ordersys_tea where 
    ordersys_order.id = order_id and tea_id = ordersys_tea.id and  time like \"'''

    raw_sql_back = "%\" group by tea_id;"

    raw_sql = raw_sql_front + time +raw_sql_back
    #print raw_sql

    cu.execute(raw_sql)


    sales = []
    for row in cu:
        sales.append(row)

    cx.close()

    # for row in sales:
    #     print row[0],row[1],row[2]


    return render(request,'stat.html',{'sales':sales})

@csrf_exempt
def statweek(request):

    cx = sqlite3.connect("/home/ray/dev/django/order_system/db.sqlite3")
    cu = cx.cursor()

    sales = []

    time = timezone.now() 
    print 'before',time

    time = time + timedelta( days = 0 )
    print 'after:',time 

    timestr = time.strftime('%Y-%m-%d')

    raw_sql_front = '''
    select ordersys_tea.id,ordersys_tea.name,sum(number) from ordersys_order,ordersys_order_tea,ordersys_tea where 
    ordersys_order.id = order_id and tea_id = ordersys_tea.id and  time like \"'''

    raw_sql_back = "%\" and tea_id = 3"

    raw_sql = raw_sql_front + timestr +raw_sql_back

    cu.execute(raw_sql)

    for row in cu:
        sales.append(row)

    time = time + timedelta( days = -1 )
    timestr = time.strftime('%Y-%m-%d')
    raw_sql = raw_sql_front + timestr +raw_sql_back
    cu.execute(raw_sql)

    for row in cu:
        sales.append(row)

    time = time + timedelta( days = -1 )
    timestr = time.strftime('%Y-%m-%d')
    raw_sql = raw_sql_front + timestr +raw_sql_back
    cu.execute(raw_sql)

    for row in cu:
        sales.append(row)


    print sales

    return render(request,'statweek.html',{'sales':sales})

@csrf_exempt 
def addorder(request):
    context ={}
    message = str(request.POST)
    context['message']=message
    username = request.POST.get('inputID','1502001')
    context['username']=username
    password = request.POST.get('inputPassword','default2')
    emp = Employee.objects.get( id = int(username) )
    context['emp']=emp

    # front order id
    time_str = timezone.now().isoformat()
    order_id_front = time_str[2:4]+time_str[5:7] 
    

    # back order id
    order_latest = Order.objects.all().order_by('-time')[:1]
    order_latest = order_latest[0]

    order_id_back = list('0000')
    #print str(order_latest.id)[4:8]
    num = int(str(order_latest.id)[4:8])+1
    i = -1
    for ch in str(num)[::-1]:
        order_id_back[i] = ch
        i = i -1

    order_id_back =  ''.join(order_id_back)

    # generate order id
    order_id = order_id_front + order_id_back
    # print order_id

    time = timezone.now()

    desk_id = request.POST.get('deskid','1')
    #print desk_id

    # calculate total price
    tid_1 = request.POST.get('select1','1')
    tea_1 = Tea.objects.get(pk=int(tid_1))
    num_1 = int(request.POST.get('number1','0'))

    tid_2 = request.POST.get('select2','1')
    tea_2 = Tea.objects.get(pk=int(tid_2))
    num_2 =int(request.POST.get('number2','0'))

    tid_3 = request.POST.get('select3','1')
    tea_3 = Tea.objects.get(pk=int(tid_3))
    num_3 = int(request.POST.get('number3','0'))

    total_price =  tea_1.price*num_1 + tea_2.price*num_2 + tea_3.price*num_3
    #print total_price

    state = 0

    employee = int(request.POST.get('select4','1502001'))

    order_new = Order.objects.create(id = order_id ,time = time, desk_id = desk_id, total_price = total_price , state = 0,employee =Employee.objects.get(id = employee))
    order_new.save()
    order_tea_new = Order_Tea.objects.create( order =  order_new , tea = tea_1 , number = num_1)
    order_tea_new.save()
    order_tea_new = Order_Tea.objects.create( order =  order_new , tea = tea_2 , number = num_2)
    order_tea_new.save()
    order_tea_new = Order_Tea.objects.create( order =  order_new , tea = tea_3 , number = num_3)
    order_tea_new.save()

    return render(request,'addorder.html',{'context':context})

