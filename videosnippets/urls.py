from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<vid>\d+)/(?P<sid>\d+)$', SnippetListView.as_view(), name='snippet-list'),
    url(r'^add/(?P<pk>\d+)', SnippetCreateView.as_view(), name='snippet-add'),
    url(r'^edit/(?P<pk>\d+)', SnippetUpdateView.as_view(), name='snippet-edit'),
    url(r'^delete/(?P<pk>\d+)', SnippetDeleteView.as_view(), name='snippet-delete'),
    url(r'^detail/(\d+)', get_snippet_title, name='snippet-detail'),
]
