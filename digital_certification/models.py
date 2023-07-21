from django.db import models

class Certificate(models.Model):
    course = models.ForeignKey('lms_app.Course', on_delete=models.CASCADE)
    student = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    issue_date = models.DateField()
    certificate_image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return f"Certificate for {self.student.username} - {self.course.title}"