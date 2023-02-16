from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from reviewme_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    '''
    Lists all the profiles
    '''

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Enables the owner to retrieve,edit or delete their profile'''
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
