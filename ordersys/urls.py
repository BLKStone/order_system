from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    #url(r'^$', views.index,  name='index'),
    url(r'^order/$',views.order, name = 'order'),
    url(r'^addorder/$',views.addorder, name = 'addorder'),
    url(r'^unfinishedorder/$',views.unfinorder, name = 'unfinorder'),
    url(r'^finishedoder/$',views.finorder, name = 'finorder'),
    url(r'^stat/$',views.stat, name = 'stat'),
    url(r'^statweek/$',views.statweek, name = 'statweek'),
    url(r'^endorder/$',views.endorder, name = 'endorder'),
    url(r'^delorder/$',views.delorder, name = 'delorder'),
    ]