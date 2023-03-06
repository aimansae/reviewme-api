from rest_framework import generics, permissions
from reviewme_api.permissions import IsOwnerOrReadOnly
from .models import Save
from .serializers import SaveSerializer


class SaveList(generics.ListCreateAPIView):
    '''
    Creates and lists savet items, only authenticated users can do that
    '''

    serializer_class = SaveSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Save.objects.all()

    def get_queryset(self, *args, **kwargs):
        return Save.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SaveDetail(generics.RetrieveDestroyAPIView):
    '''
    Enables the owner to retreve or delete a saved product
    '''
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()
    
    def get_queryset(self, *args, **kwargs):
        return Save.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
