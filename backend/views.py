from django.shortcuts import render
from rest_framework import viewsets
from .models import Workout, Exercise, Set
from .serializers import WorkoutSerializer, ExereciseSerializer, SetSerializer

# Create your views here.
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExereciseSerializer
    
class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer        