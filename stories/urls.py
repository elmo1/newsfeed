from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'stories.views.index'),
    url(r'^story/$', 'stories.views.story'),
    url(r'^vote/$', 'stories.views.vote'),
    url(r'^s/(?P<category_name>\w+)/$', 'stories.views.category'),
    url(r'^s/(?P<category_name>\w+)/(?P<story_id>[0-9]+)/$', 'stories.views.comment'),
    url(r'^u/(?P<username>\w+)/$', 'stories.views.profile'),
]