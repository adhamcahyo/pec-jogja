from django.db import models

class CourseSentiment(models.Model):
    course = models.ForeignKey('lms_app.Course', on_delete=models.CASCADE)
    positive_reviews = models.IntegerField(default=0)
    negative_reviews = models.IntegerField(default=0)

    def __str__(self):
        return f"Sentiment analysis for {self.course.title}"