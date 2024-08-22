from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getNoteDetail(request, pk):
    note = get_object_or_404(Note, id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createNote(request):
    data = request.data
    
    # Check if 'body' field is empty or not provided
    if 'body' not in data or not data['body'].strip():
        return Response({'message': 'Data required: body field cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = NoteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateNote(request, pk):
    note = get_object_or_404(Note, id=pk)
    data = request.data
    serializer = NoteSerializer(instance=note, data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = get_object_or_404(Note, id=pk)
    note.delete()
    return Response({'message': 'Note was deleted!'}, status=status.HTTP_204_NO_CONTENT)
