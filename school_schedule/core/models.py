from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    grades = models.ManyToManyField(Subject, through="Grade")

    def __str__(self):
        return self.name

class Schedule(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class_group = models.ForeignKey('Class', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=9)  # Додаємо це поле

    def __str__(self):
        return f"{self.class_group} - {self.subject} ({self.day_of_week})"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.student}'s grade in {self.subject} is {self.grade}"