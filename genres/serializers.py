from rest_framework import serializers

from .models import Genre


class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
