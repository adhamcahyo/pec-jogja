from django.db import models

class MachineLearningAssessment(models.Model):
    assignment = models.ForeignKey('lms_app.Assignment', on_delete=models.CASCADE)
    student = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField()

    def __str__(self):
        return f"Assessment for {self.assignment.title} by {self.student.username}"