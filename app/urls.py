from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_activities', views.get_activities, name='get_activities'),
]

urlpatterns += staticfiles_urlpatterns()
