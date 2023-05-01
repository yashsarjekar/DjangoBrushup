from django.urls import path
from .views import MyView, WebScrap, WebScrapResult, MyViewResult

urlpatterns = [
    path('myview/', MyView.as_view()),
    path('myview_result/', MyViewResult.as_view()),
    path('webscrap/', WebScrap.as_view()),
    path('webscrap_result/', WebScrapResult.as_view()),
]