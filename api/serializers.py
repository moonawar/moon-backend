from django.db.models import fields
from rest_framework import serializers
from .models import Dialogue

class DialogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialogue
        fields = ['by', 'page', 'context','text']