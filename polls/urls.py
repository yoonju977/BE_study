
from django.urls import path
from . import views

urlpatterns = [
    path("<int:question_id>/", views.detail, name="detail"),
]
# ex: /polls/5/ path("<int:question_id>/", views.detail, name="detail"),