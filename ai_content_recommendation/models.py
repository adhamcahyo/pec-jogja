from django.db import models

class RecommendedCourse(models.Model):
    user = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    course = models.ForeignKey('lms_app.Course', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Recommended course for {self.user.username} - {self.course.title}"