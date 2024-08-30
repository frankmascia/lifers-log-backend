from rest_framework import serializers
from .models import Workout, Exercise, Set

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ['id', 'weight', 'repetitions']

class ExereciseSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields =['id', 'name', 'sets']

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExereciseSerializer(many=True, read_only = True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'date', 'exercises']
