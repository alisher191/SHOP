from bdb import effective
from email.policy import default
from .models import Noutbuk
from rest_framework import serializers
from .models import Noutbuk

class NoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Noutbuk
        fields = '__all__'

class NoutListlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noutbuk
        fields = ('id', 'name', 'user')


class NoutDeteilSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Noutbuk
        fields = '__all__'