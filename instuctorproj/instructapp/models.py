from django.db import models
from users.models import User

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    start_date = models.DateField(null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught')
    enrolled = models.ManyToManyField(User, related_name='courses_enrolled', blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.title

# Lesson Model
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    due_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title + ' (' + self.course.title + ')'

# Lesson Supporting Media Model
class LessonUploads(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='uploads')
    title = models.CharField(max_length=100)
    media = models.FileField()

    def __str__(self):
        return self.title + ' (' + self.lesson.title + ')'


# Student Submission/Feedback Model
class StudentSubmission(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    submission = models.FileField()
    feedback = models.TextField()

    def __str__(self):
        return self.student + ' (' + self.lesson.title + ')'