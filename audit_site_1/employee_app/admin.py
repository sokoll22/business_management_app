from django.contrib import admin

from .models import Employee, Category, JobPosition

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'job_status', 'rate', 'bonus',
                    'bar_bonus', 'notes', 'employee_status', 'created_at', 'updated_at')
    list_display_links = ('id', 'last_name')
    search_fields = ('id', 'last_name', 'position', 'rate', 'bonus', 'employee_status')
    list_editable = ('employee_status',)
    list_filter = ('position', 'job_status', 'rate')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(JobPosition, JobPositionAdmin)



