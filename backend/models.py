from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name} on {self.date}"

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='sets', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    repititions = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.repititions} reps at {self.weight} lb"