from django.urls import path
from .views import WeightView

urlpatterns = [
    path('api/weight/', WeightView.as_view(), name='weight_api'),
]
