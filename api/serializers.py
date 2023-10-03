from rest_framework import serializers
from base.models import Diaspora, County

class DiasporaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diaspora
        fields = '__all__'


class  CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'