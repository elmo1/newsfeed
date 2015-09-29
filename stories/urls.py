from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'stories.views.index'),
    url(r'^story/$', 'stories.views.story'),
    url(r'^vote/$', 'stories.views.vote'),
    url(r'^(?P<category_name>\w+)/$', 'stories.views.category'),
    #url(r'^/(?P<slug>[\w-]+)/$', 'stories.views.category'),
]