from django.db import models
from django.utils import timezone

#class CustomManager(models.Manager):
 # def get_queryset(self):	# overriding Built-in method called when we call all()
  #   return super().get_queryset().order_by('name')
  
class CustomManager(models.Manager):
 def get_students_percentage_range(self, r1, r2):
  return super().get_queryset().filter(percentage__range=(r1, r2))
 
class StudentsQuerySet(models.QuerySet):
   def name_list(self):
      return self.filter(name='ram')

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subjects=models.CharField(max_length=100)
    percentage=models.IntegerField()
    admited = models.DateTimeField(default=timezone.now)

    objects = models.Manager()			# Default Manager
    students = CustomManager()		# Custom Manager

class Meta:
    ordering=('-admited',)
    def __str__(self) :
        return self.name