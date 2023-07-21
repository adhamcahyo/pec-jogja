from django.db import models

class AdaptiveCourse(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class AdaptiveLesson(models.Model):
    course = models.ForeignKey(AdaptiveCourse, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title