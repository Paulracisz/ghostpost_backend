from rest_framework import serializers

from ghostpost.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'description',
            'roast_or_boast',
            'up_vote',
            'down_vote',
            'time_created'
        ]