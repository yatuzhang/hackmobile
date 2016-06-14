from django.conf.urls import url
from mlearn import views

urlpatterns = [
    url(r'^mlearn/$', views.mlearn_list),
    url(r'^mlearn/(?P<pk>[0-9]+)/$', views.mlearn_detail),
]