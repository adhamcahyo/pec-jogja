from django.db import models

class StudentPerformance(models.Model):
    student = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    course = models.ForeignKey('lms_app.Course', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    time_spent = models.DurationField()

    def __str__(self):
        return f"Performance of {self.student.username} in {self.course.title}"