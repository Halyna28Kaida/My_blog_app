from django.urls import path
from myapp.views import index, about, create, topics

urlpatterns = [
    path("", index),
    path("about/", about),
    path("create/", create),
    path("topics", topics)
]
