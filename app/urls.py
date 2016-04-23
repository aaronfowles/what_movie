from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_activities', views.get_activities, name='get_activities'),
    url(r'^record_selection', views.record_selection, name='record_selection'),
    url(r'^database', views.database, name='database'),
    url(r'^add_activity', views.add_activity, name='add_activity'),
    url(r'^add_tag', views.add_tag, name='add_tag'),
]

urlpatterns += staticfiles_urlpatterns()
