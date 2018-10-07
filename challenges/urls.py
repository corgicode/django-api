from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'challenges', views.ChallengesViewSet, base_name='Challenges')

urlpatterns = [
    url(r'^', include(router.urls)),
]
