from django.urls import path
from .views import GetDialogueView, CreateDialogueView, UpdateDialogue, DialoguePage
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('dialogue/create', CreateDialogueView.as_view()),
    path('dialogue/', GetDialogueView.as_view()),
    path('dialogue/<str:page>', DialoguePage.as_view()),
    path('dialogue/update/', UpdateDialogue.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)