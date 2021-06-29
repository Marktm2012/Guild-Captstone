from django.contrib import admin
from .models import Course, Lesson, LessonUploads, StudentSubmission


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonUploads)
admin.site.register(StudentSubmission)
