from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from rest_framework import routers
from accounts.views import (
        UserViewSet, UserProfileViewSet, GroupViewSet
)

from conversation.views import (
        ChannelViewSet, ChannelMessageViewSet
)
from ownership.views import UserBookViewSet, MyBookViewSet
from catalog.views import BookViewSet, CategoryViewSet
from communities.views import CommunityViewSet, MembershipViewSet
from transaction.views import TransactionViewSet
from reservation.views import LoanRequestViewSet

# API routers URL
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users-profile', UserProfileViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'conversations', ChannelViewSet)
router.register(r'messages', ChannelMessageViewSet)
router.register(r'books', BookViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'user-books', UserBookViewSet)
router.register(r'my-books', MyBookViewSet, base_name='mybook')
router.register(r'communities', CommunityViewSet)
router.register(r'membership', MembershipViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'reservation', LoanRequestViewSet)
resource_urlpatterns = router.urls

# API customs views URL
custom_api_urlpatterns = patterns('',
    url(r'^$', 'bookshare.views.api_root',
        name='api-root'),

    url(r'^register/', 'accounts.views.user_registration',
        name='user-registration'),

    # Search for Book from Google Book Service.
    url(r'^search/provider/', 'catalog.views.book_provider',
        name='search-provider'),

    # Search for Book from Book Share System
    url(r'^search/', 'catalog.views.search', name='search'),

)


# URL for REST API
api_urlpatterns = custom_api_urlpatterns + resource_urlpatterns


# URL for specific Django Apps
app_urlpatterns = patterns('',

    url(r'^admin/',
        include(admin.site.urls)),

    url(r'^oauth2/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^auth/',
        include('rest_framework.urls', namespace='rest_framework')),

    url(r'^token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

    url('', include('social.apps.django_app.urls', namespace='social')),

)

urlpatterns = api_urlpatterns + app_urlpatterns


########################################
# Local Development URL Configurations #
########################################
urlpatterns += staticfiles_urlpatterns()
