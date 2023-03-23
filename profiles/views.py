from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from reviewme_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count

# Credit C.I. DRF-API walkthrough.


class ProfileList(generics.ListAPIView):
    '''
    Lists all the profiles, counts number of reviews per profile
    '''

    queryset = Profile.objects.annotate(
        reviews_count=Count('owner__review', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    # filter
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'reviews_count'
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Enables the owner to retrieve,edit or delete their profile
    '''

    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        reviews_count=Count('owner__review', distinct=True)
    ).order_by('-created_at')

    permission_classes = [IsOwnerOrReadOnly]
