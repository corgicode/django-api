from rest_framework import viewsets
from .models import Challenge
from .serializers import ChallengeSerializer

class ChallengesViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Challenge.objects.all()
        pk = self.request.query_params.get('pk', None)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        return queryset

    serializer_class = ChallengeSerializer
