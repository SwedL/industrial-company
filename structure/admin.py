from django.contrib import admin
from .models import Position, Employee

# Register your models here.


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'vacancies', 'base_salary', 'boss', 'is_manager')
    fields = ('boss', 'name', 'vacancies', 'base_salary', 'is_manager', )
    list_display_links = ('name', 'boss', 'vacancies', 'base_salary')
    ordering = ('id', )
    # list_per_page = 10


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    # readonly_fields = ('date',)
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'position', 'employment_date', 'pos_rel', 'salary')
    fields = ('last_name', 'first_name', 'patronymic', 'position', 'salary')
    search_fields = ('last_name', 'first_name', 'salary')
    ordering = ('id',)
    # list_per_page = 10

    @admin.display(ordering='id', description='непосредственный начальник')
    def pos_rel(self, emp: Employee):
        return emp.position.boss



admin.site.site_title = 'Администрирование Aquamarine structure'
