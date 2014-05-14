from django.conf.urls import patterns, include, url
from rest_framework import routers
from api.v1 import views

from rest_framework import viewsets
from comm.models import Conversation

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users-profile', views.UserProfileViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'conversations', views.ConversationViewSet)
router.register(r'messages', views.ConversationMessageViewSet)
router.register(r'reservations', views.BookReservationViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'books-profile', views.BookProfileViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = patterns('',
    url(r'^',
        include(router.urls)),
)
