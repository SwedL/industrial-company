from django.contrib import admin

from structure.models import Employee, Position

# Register your models here.


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vacancies', 'base_salary', 'boss', 'is_manager')
    fields = ('boss', 'name', 'vacancies', 'base_salary', 'is_manager',)
    list_display_links = ('name', 'boss', 'vacancies', 'base_salary')
    ordering = ('id',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'position', 'employment_date', 'pos_rel', 'salary')
    fields = ('last_name', 'first_name', 'patronymic', 'position', 'salary')
    search_fields = ('last_name', 'first_name', 'salary')
    list_display_links = (
        'id',
        'last_name',
        'first_name',
        'patronymic',
        'position',
        'employment_date',
        'pos_rel',
        'salary',
    )
    ordering = ('id',)

    @admin.display(ordering='id', description='непосредственный начальник')
    def pos_rel(self, emp: Employee):
        try:
            res = emp.position.boss
        except AttributeError:
            res = None
        return res
