from django.contrib import admin
from srmsApp import models
from .models import Class
from .models import Subject
from .models import Student
from .models import Result
from .models import Student_Subject_Result
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(models.Class)
# admin.site.register(models.Subject)
# admin.site.register(models.Student)
# admin.site.register(models.Result)
# admin.site.register(models.Student_Subject_Result)
@admin.register(Class)
class yeardata(ImportExportModelAdmin):
    pass

@admin.register(Subject)
class subjectdata(ImportExportModelAdmin):
    pass

@admin.register(Student)
class studentdata(ImportExportModelAdmin):
    pass

@admin.register(Result)
class resultdata(ImportExportModelAdmin):
    pass

@admin.register(Student_Subject_Result)
class studentsubjcetresultdata(ImportExportModelAdmin):
    pass