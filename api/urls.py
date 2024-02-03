from django.urls import path
from .views import ArticleList, ArticleDetails
urlpatterns = [
    path('<int:pk>/', ArticleDetails.as_view()),
    path('', ArticleList.as_view()),
    path('<int:pk>/', ArticleDetails.as_view()),

]