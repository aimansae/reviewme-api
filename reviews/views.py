from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from reviewme_api.permissions import IsOwnerOrReadOnly


class ReviewList(generics.ListCreateAPIView):

    '''
    Lists all the revies and enables to create them if user is logged in
    '''
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Enables to retrieve, edit or delete a revie to the owner
    '''
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
