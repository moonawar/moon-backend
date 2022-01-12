from django.urls import path
from .views import GetDialogueView, CreateDialogueView, UpdateDialogueView

urlpatterns = [
    path('dialogue/create', CreateDialogueView.as_view()),
    path('dialogue/get/', GetDialogueView.as_view()),
    path('dialogue/update/', UpdateDialogueView.as_view()),
]