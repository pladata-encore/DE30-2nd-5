from django.urls import path, include
from .views import symptom, disease

urlpatterns = [
    path("symptom/", symptom),
    path("disease/", disease)

]
