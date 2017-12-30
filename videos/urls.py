from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', VideoListView.as_view(), name='video-list'),
    url(r'^add', VideoCreateView.as_view(), name='video-add'),
    url(r'^edit/(?P<pk>\d+)', VideoUpdateView.as_view(), name='video-edit'),
    url(r'^delete/(?P<pk>\d+)', VideoDeleteView.as_view(), name='video-delete'),
]