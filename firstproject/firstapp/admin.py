from django.contrib import admin

from .models import Course, Instructor, Lesson

# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3
    
class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)

