from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    school = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    addmission_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)
