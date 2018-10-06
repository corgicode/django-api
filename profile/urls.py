from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'profiles', views.ProfileViewSet, base_name='Profile')

urlpatterns = [
    url(r'^', include(router.urls)),
]
