from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    '''
    Shows the contact requests sent by the owner of the form
    '''
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get_queryset(self, *args, **kwargs):
        return Contact.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
