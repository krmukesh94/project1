from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^teacher$', views.teacher, name='teacher'),
    url(r'^student$', views.student, name='student'),
]