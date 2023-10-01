from rest_framework import serializers
from base.models import Diaspora

class DiasporaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diaspora
        fields = '__all__'

    