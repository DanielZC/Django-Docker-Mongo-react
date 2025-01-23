from django.urls import path
from .views import register_user, get_user, db_vars

urlpatterns = [
    path("user/", register_user),
    path("db/vars/", db_vars),
    path("get/user/", get_user),
]
