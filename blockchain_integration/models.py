from django.db import models

class Transcript(models.Model):
    student = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    courses = models.ManyToManyField('lms_app.Course', related_name='transcripts')
    issue_date = models.DateField()
    hash_value = models.CharField(max_length=100)

    def __str__(self):
        return f"Transcript for {self.student.username}"