from django.db import models

class Student(models.Model):
    first_name=models.charField(max_length=12)
    last_name=models.charField(max_length=20)
    age=models.positiveSmallIntergerField()
    date_of_birth=models.DateField()