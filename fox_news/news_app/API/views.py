from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets
from news_app.models import NewsDetails
from news_app.API.serializers import NewsDetailsSerializer


class NewsDetailsView(ListAPIView):
    queryset = NewsDetails.objects.all()
    serializer_class = NewsDetailsSerializer
