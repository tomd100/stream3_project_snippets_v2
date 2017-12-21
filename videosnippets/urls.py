from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)$', SnippetListView.as_view(), name='snippet-list'),
    url(r'^$', SnippetDetailView.as_view(), name='snippet-detail'),
    url(r'^add', SnippetCreateView.as_view(), name='snippet-add'),
    url(r'^(?P<pk>\d+)/edit', SnippetUpdateView.as_view(), name='snippet-edit'),
    url(r'^(?P<pk>\d+)/delete', SnippetDeleteView.as_view(), name='snippet-delete'),
]
