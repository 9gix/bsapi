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

# API routers URL
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users-profile', UserProfileViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', ConversationMessageViewSet)
router.register(r'books-profile', BookProfileViewSet)
router.register(r'books', BookViewSet)
router.register(r'communities', CommunityViewSet)
resource_urlpatterns = router.urls

# API customs views URL
custom_api_urlpatterns = patterns('',

    url(r'^search',
        'catalog.views.search', name='search'),

)


# URL for REST API
api_urlpatterns = resource_urlpatterns + custom_api_urlpatterns


# URL for specific Django Apps
app_urlpatterns = patterns('',

    url(r'^admin/',
        include(admin.site.urls)),

    url(r'^oauth2/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^auth/',
        include('rest_framework.urls', namespace='rest_framework')),

)

# URL for static serving on dev environments
static_urlpatterns = staticfiles_urlpatterns()


urlpatterns = api_urlpatterns + app_urlpatterns + static_urlpatterns
