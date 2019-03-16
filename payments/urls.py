from django.urls import path,include
from .views import *

app_name = "payments"

urlpatterns = [
    path('charge/',charge,name="Make payment")
]