from django.urls import path
from . import views

app_name="polls"

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("add_question/",views.add_question, name="add_question"),
    path("<int:question_id>/add_choice/", views.add_choice, name="add_choice"),
    path("update_question/", views.update_question, name="update_question"),
    path("delete_question/", views.delete_question, name="delete_question"),
]