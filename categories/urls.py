from django.conf.urls import url
from .views import *
from videos.views import VideoListView

urlpatterns = [
    # url(r'^$', VideoListView.as_view(), name='videocategory-list'),
    url(r'^add', VideoCategoryCreateView.as_view(), name='videocategory-add'),
    url(r'^edit/(?P<pk>\d+)', VideoCategoryUpdateView.as_view(), name='videocategory-edit'),
    url(r'^delete/(?P<pk>\d+)', VideoCategoryDeleteView.as_view(), name='videocategory-delete'),
    # url(r'^edit', VideoCategoryUpdateView.as_view(), name='videocategory-edit'),
    # url(r'^delete', VideoCategoryDeleteView.as_view(), name='videocategory-delete'),

]