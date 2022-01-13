from django.db.models import fields
from rest_framework import serializers
from .models import Dialogue

class DialogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialogue
        fields = ['id','by', 'page', 'context','text', 'order','trigger']