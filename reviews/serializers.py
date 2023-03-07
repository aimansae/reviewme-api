from rest_framework import serializers
from .models import Review
from likes.models import Like
from save.models import Save


class ReviewSerializer(serializers.ModelSerializer):
    '''
    Review model Serialization
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    likes_created_at = serializers.ReadOnlyField()
    save_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, review=obj
            ).first()
            return like.id if like else None
        return None
    
    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, review=obj
            ).first()
            return save.id if save else None
        return None
    # image validation code from C.I walkthrough
    # and Django rest field validation docs

    def validate_image(self, value):
        if (value.size) > (1024 * 1024 * 2):
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
            
        if (value.image.width) > 4096:
            raise serializers.ValidationError(
                'Image size larger than 4096px!'
            )
            
        if (value.image.height) > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    class Meta:
        model = Review
        fields = [
            'id',
            'is_owner',
            'profile_id',
            'profile_image',
            'owner',
            'product_title',
            'description',
            'image',
            'price',
            'rating',
            'like_id',
            'created_at',
            'updated_at',
            'likes_count',
            'comment_count',
            'likes_created_at',
            'save_id'
        ]  # or '__all_'
