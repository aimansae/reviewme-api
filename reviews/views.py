from rest_framework import generics, permissions, filters
from .models import Review
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ReviewSerializer
from reviewme_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class ReviewList(generics.ListCreateAPIView):

    '''
    Lists all the reviews and enables to create them if user is logged in
    '''
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
# to check saved owner
    filterset_fields = [
        'likes__owner__profile',
        'saved__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'product_title'
    ]
    ordering_fields = [
        'likes_count',
        'comment_count',
        'likes_created_at',

    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Enables to retrieve, edit or delete a revie to the owner
    '''
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('created_at')
