from rest_framework import serializers
from .models import Chat


class ChateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        extra_kwargs ={
            'user':{'required':False},
            "prodict":{'required':False}
        }
