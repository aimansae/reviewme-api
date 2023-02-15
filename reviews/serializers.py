from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    '''
    Review model Serialization
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    # image validation code from C.I walkthrough
    # and Django rest field validation docs
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image size larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value
            
            
            
            
    class Meta:
        model = Review
        fields = [
            'id',
            'owner',
            'product_title',
            'description',
            'image',
            'price',
            'rating',
            'created_at',
            'modified_on',
        ]  # or '__all_'
