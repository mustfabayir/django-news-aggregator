from django.urls import path
from news_app.API.views import NewsDetailsView

urlpatterns = [
    path('news/', NewsDetailsView.as_view(), name = 'news'),
]