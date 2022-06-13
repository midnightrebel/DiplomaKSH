from django.contrib import admin
from import_export import resources
from .models import Students
from .models import Students,Groups,Teachers
admin.site.register(Students)
admin.site.register(Groups)
# Register your models here.
class StudentResource(resources.ModelResource):

    class Meta:
        model = Students