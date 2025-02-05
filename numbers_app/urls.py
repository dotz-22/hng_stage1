from django.urls import path
from .views import ClassifyView

urlpatterns = [
    path('classify-number/', ClassifyView.as_view(), name='classify-number'),
]