from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

''' Function Based Views
urlpatterns = patterns('apps.snippets_tutorial.views',
    url(r'^snippets_tutorial/$', 'snippet_list'),
    url(r'^snippets_tutorial/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)
'''


# VIEW endpoints
urlpatterns = format_suffix_patterns(patterns('apps.snippets_tutorial.views',
    url(r'^$', 'api_root'),
    url(r'^snippets_tutorial/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets_tutorial/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets_tutorial/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
))

# VIEW-SET endpoints
urlpatterns = format_suffix_patterns(patterns('apps.snippets_tutorial.views',
    url(r'^$', 'api_root'),
    url(r'^snippets_tutorial/$', views.snippet_list, name='snippet-list'),
    url(r'^snippets_tutorial/(?P<pk>[0-9]+)/$', views.snippet_detail, name='snippet-detail'),
    url(r'^snippets_tutorial/(?P<pk>[0-9]+)/highlight/$', views.snippet_highlight, name='snippet-highlight'),
    url(r'^users/$', views.user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail, name='user-detail')
))