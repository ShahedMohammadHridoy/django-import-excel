from django.db import models


class Student(models.Model):
    std_id = models.CharField(
        max_length=11, null=True, blank=True
    )
    student_name = models.CharField(
        max_length=100, null=True, blank=True
    )
    contact_number = models.CharField(
        max_length=11, null=True, blank=True
    )

    def __str__(self):
        return self.student_name