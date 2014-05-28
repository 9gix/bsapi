from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from rest_framework import routers

from accounts.views import (
        UserViewSet, UserProfileViewSet, GroupViewSet
)
from comm.views import (
        ConversationViewSet, ConversationMessageViewSet
)
from ownership.views import BookViewSet
from catalog.views import BookProfileViewSet

from communities.views import CommunityViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users-profile', UserProfileViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', ConversationMessageViewSet)
router.register(r'books-profile', BookProfileViewSet)
router.register(r'books', BookViewSet)
router.register(r'communities', CommunityViewSet)


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^auth/', 
        include('rest_framework.urls', namespace='rest_framework')),

    url(r'^',
        include(router.urls)),

#    url(r'^$', 'bookshare.views.api_root', name='api-root'),

) + staticfiles_urlpatterns()
