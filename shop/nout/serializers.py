from .models import Noutbuk
from rest_framework import serializers
from .models import Noutbuk

class NoutListlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noutbuk
        fields = ('id', 'name', 'user')


class NoutDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noutbuk
        fields = '__all__'