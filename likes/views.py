from rest_framework import generics, permissions
from reviewme_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    '''
    Creates and lists likes, only authenticated users can do that
    '''

    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    '''
    Enables to retreve or delete a like to the owner
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
