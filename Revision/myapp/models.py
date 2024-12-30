from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    city=models.CharField(max_length=50)
    feedback=models.TextField()
    def __str__(self):
        return self.name