from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
