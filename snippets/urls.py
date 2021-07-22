from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views
from snippets.views import SnippetList, SnippetDetail, index

urlpatterns = [
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^index/$', index),
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)