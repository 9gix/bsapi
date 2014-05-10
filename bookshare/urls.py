from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'oauth2/', include('provider.oauth2.urls', namespace='oauth2')),

    url(r'^api/auth/', 
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/',
        include('api.urls', namespace='api')),

    url(r'^$', 'bookshare.views.home', name='homepage'),

) + staticfiles_urlpatterns()
