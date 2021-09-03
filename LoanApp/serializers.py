from rest_framework import serializers
from .models import ModelFeatures


class ModelFeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelFeatures
        fields = "__all__"


