from  django.urls import path
from .views import register_student


urlpatterns=[
    path("regster/", register_student, name="register_student"),
]