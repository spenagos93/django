from django.urls import path
from . import views
#rutas de la app polls

app_name = "polls"

urlpatterns = [
    #example: /polls
    path("", views.IndexView.as_view(), name="index"),
    #example: /polls/5/
    path("<int:pk>/details", views.DetailsView.as_view(), name="details"),
    #example: /polls/5/results/
    path("<int:pk>/results", views.ResultView.as_view(), name="results"),
    #example: /polls/5/votes/
    path("<int:question_id>/vote", views.vote, name="vote")
]
