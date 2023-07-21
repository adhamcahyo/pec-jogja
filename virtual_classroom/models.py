from django.db import models

class VirtualClassroom(models.Model):
    course = models.ForeignKey('lms_app.Course', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    instructor_link = models.URLField()
    student_link = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.course.title}"