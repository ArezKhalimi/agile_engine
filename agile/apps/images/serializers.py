from rest_framework import serializers

from agile.apps.images.models import Image, HashTag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ['tag_name']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(read_only=True, many=True, source='hashtags')
    id = serializers.CharField(source='pcid')

    class Meta:
        model = Image
        fields = [
            'id', 'title', 'picture', 'camera', 'author', 'tags',
            'last_activity'
        ]
