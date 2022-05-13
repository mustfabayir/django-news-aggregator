from rest_framework import serializers
from news_app.models import NewsDetails

class NewsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetails
        fields = '__all__'