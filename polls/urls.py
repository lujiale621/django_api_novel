from django.urls import path
from polls.views import *
from . import views
urlpatterns = [
    path('e1searchbook',NovelSearchBookView.as_view()),
    path('e1bookdetail', NovelSearchBookDetailView.as_view()),
    path('e1bookcontent', NovelSearchBookContentView.as_view()),
    path('e1booksort', NovelSearchBookSort.as_view()),
    path('e1bookrank1', NovelSearchBookRank1.as_view()),
    path('e1bookrank2', NovelSearchBookRank2.as_view()),
]