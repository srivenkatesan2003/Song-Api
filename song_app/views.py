from django.shortcuts import render
from rest_framework import generics            # we can  using this way
from rest_framework.viewsets import ModelViewSet # we can  using this way
from .models import song
from .serializer import songserialzer
# Create your views here.

# class SongListCreateViews(ModelViewSet):
#     queryset = song.objects.all()
#     serializer_class = songserialzer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = song.objects.all()
    serializer_class = songserialzer

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = song.objects.all()
    serializer_class = songserialzer

def song_list(request):
    songs = song.objects.all()
    return render(request,'song_list.html', {'songs': songs})