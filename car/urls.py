from django.urls import path, include
from .views import (
    carIndex
)


urlpatterns = [
    path('', carIndex, name='carIndex')
]