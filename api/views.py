from django.http import request
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Dialogue
from api.serializers import DialogueSerializer

# Create your views here.
class DialoguePage(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get_list(self, page):
        try:
            return Dialogue.objects.filter(page=page)
        except Dialogue.DoesNotExist:
            raise Http404
    
    def get(self, request, page, format=None):
        dialogues = self.get_list(page)
        serializer = DialogueSerializer(dialogues, many=True)
        return Response(serializer.data)

class CreateDialogueView(generics.CreateAPIView):
    queryset = Dialogue.objects.all()
    serializer_class = DialogueSerializer


class GetDialogueView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        dialogues = Dialogue.objects.all().order_by('id')
        serializer = DialogueSerializer(dialogues, many=True)
        return Response(serializer.data)

class UpdateDialogue(APIView):
    def get_object(self, id):
        try:
            return Dialogue.objects.get(id=id)
        except Dialogue.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        dialogue = self.get_object(id)
        serializer = DialogueSerializer(dialogue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        dialogue = self.get_object(id)
        dialogue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)