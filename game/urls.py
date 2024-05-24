from django.urls import path,include
from game.views import index,game
urlpatterns = [
    path('',index),
    path("game/<int:id>/<str:name>/",game)
]

