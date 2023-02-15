from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Profile model Serialization
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
        
    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'name',
            'description',
            'country',
            'image',
            'is_owner',
        ]  # or '__all_'
