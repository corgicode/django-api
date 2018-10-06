from rest_framework import viewsets
from .models import Profile, ProfileURL
from .serializers import ProfileSerializer, ProfileURLSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileURLsViewSet(viewsets.ModelViewSet):
    queryset = ProfileURL.objects
    serializer_class = ProfileURLSerializer

    def get_queryset(self):
        queryset = super(ProfileURL, self).get_queryset()

        if 'profile_pk' in self.kwargs:
            order_pk = self.kwargs['profile_pk']
            queryset = queryset.filter(profile__pk=order_pk)

        return queryset
