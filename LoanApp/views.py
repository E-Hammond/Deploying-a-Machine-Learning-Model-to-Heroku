from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import ModelFeatures
from rest_framework import serializers

from .serializers import ModelFeaturesSerializer


class PredictorView(APIView):
    ModelFeatures = ModelFeaturesSerializer

    def get(self, request):
        features = ModelFeatures.objects.all()
        serializer_class = ModelFeaturesSerializer(features, many=True)
        return Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        gender = request.data.get('gender')
        married = request.data.get('married')

        # data = {
        #     "gender": gender,
        #     "married": married
        # }

        data = request.data
        serializer = ModelFeaturesSerializer(data=data)
        if data['gender'] != "Male" and data['gender'] != 'Female':
            raise serializers.ValidationError({"Please Enter Male or Female"})
        elif data['married'] != 'Yes' and data['married'] != 'No':
            raise serializers.ValidationError({"Please Enter Yes or No"})
        elif serializer.is_valid():
            serializer.save()
            return Response({'message': 'Created successfully', 'content': serializer.data['gender']})
        return Response(serializer.errors)


