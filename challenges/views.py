from rest_framework import viewsets
from .models import Challenge, Tag
from .serializers import ChallengeSerializer, TagGetSerializer

class ChallengesViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Challenge.objects.filter(is_visible=True,).order_by('id')
        pk = self.request.query_params.get('pk', None)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        return queryset

    serializer_class = ChallengeSerializer

    class Meta:
        ordering = ['-id']

class TagsViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Tag.objects.all().order_by('id')
        pk = self.request.query_params.get('name', None)
        if pk is not None:
            queryset = queryset.filter(name=name)
        return queryset

    serializer_class = TagGetSerializer

    class Meta:
        ordering = ['-id']

