from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', VideoListView.as_view(), name='video-list'),
    url(r'^add', VideoCreateView.as_view(), name='video-add'),
    url(r'^(?P<pk>\d+)/edit', VideoUpdateView.as_view(), name='video-edit'),
    url(r'^(?P<pk>\d+)/delete', VideoDeleteView.as_view(), name='video-delete'),
]