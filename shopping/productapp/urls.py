from django.urls import path
from productapp import views

urlpatterns=[
    path("product",views.index)
]