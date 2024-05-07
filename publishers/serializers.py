from rest_framework import serializers

from .models import Publisher


class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"
