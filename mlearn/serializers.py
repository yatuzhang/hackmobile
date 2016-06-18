from rest_framework import serializers
from mlearn.models import Mlearn
from PIL import Image
import PIL
class MlearnSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    experiment_text = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    
    def create(self, validated_data):
        """
        Create and return a new `Mlearn` instance, given the validated data.
        """
        return Mlearn.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Mlearn` instance, given the validated data.
        """
        instance.experiment_text = validated_data.get('experiment_text', instance.experiment_text)
        instance.image = valiadate_data.get('image', instance.image)
        instance.save()
        return instance
