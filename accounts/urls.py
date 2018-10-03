from django.conf.urls import url, include
from accounts import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet, base_name='User')

urlpatterns = [
    url(r'^', include(router.urls)),
]
