from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    

    class Meta:

        model = Contact
        fields = [
            'owner',
            'is_owner',
            'id',
            'full_name',
            'email', 'phone',
            'query_text',
            'created_at',
        ]
