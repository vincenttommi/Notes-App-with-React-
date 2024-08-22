from django.urls import path
from . import views 





urlpatterns  = [
    path('get_notes/', views.getNotes, name='getNotes'),
    path('get_note_detail/<int:pk>/', views.getNoteDetail, name='getNoteDetail'),
    path('create/', views.createNote, name='createNote'),
    path('update/<int:pk>/', views.updateNote, name='updateNote'),
    path('delete/<int:pk>/', views.deleteNote, name='deleteNote')
]