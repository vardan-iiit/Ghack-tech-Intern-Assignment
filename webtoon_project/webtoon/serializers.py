from rest_framework import serializers
from .models import Webtoon

class WebtoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webtoon
        fields = ['id', 'title', 'description', 'characters']
