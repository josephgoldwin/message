from django.urls import path

from . import views


urlpatterns = [
    path("", views.error, name="error_message"),
    path("success/", views.success, name="success"),
    path("info/", views.info, name="info"),
    path("danger/", views.danger, name="danger"),
    path("warning/", views.warning, name="warning"),
]