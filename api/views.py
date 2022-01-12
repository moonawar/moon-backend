from django.db.models import query
from django.http import request
from django.shortcuts import render
from rest_framework import generics, serializers

from api.models import Dialogue
from api.serializers import DialogueSerializer

# Create your views here.
class CreateDialogueView(generics.CreateAPIView):
    queryset = Dialogue.objects.all()
    serializer_class = DialogueSerializer

class GetDialogueView(generics.ListAPIView):
    serializer_class = DialogueSerializer
    queryset = Dialogue.objects.all()

class UpdateDialogueView(generics.UpdateAPIView):
    queryset = Dialogue.objects.all()
    serializer_class = DialogueSerializer