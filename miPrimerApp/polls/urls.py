from django.urls import path
from . import views
#rutas de la app polls
app_name = "polls"
urlpatterns = [
    #example: /polls
    path("", views.index, name="index"),
    #example: /polls/5/
    path("<int:question_id>/details", views.details, name="details"),
    #example: /polls/5/results/
    path("<int:question_id>/results", views.results, name="results"),
    #example: /polls/5/votes/
    path("<int:question_id>/vote", views.vote, name="vote")

]
