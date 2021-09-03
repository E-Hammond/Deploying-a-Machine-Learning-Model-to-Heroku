from django.urls import path

from .views import PredictorView

urlpatterns = [
    path('predict/', PredictorView.as_view(), name='predictor')
]