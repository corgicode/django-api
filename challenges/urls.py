from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'challenges', views.ChallengesViewSet, base_name='Challenges')
router.register(r'tags', views.TagsViewSet, base_name='Tags')

urlpatterns = [
    url(r'^', include(router.urls)),
]
