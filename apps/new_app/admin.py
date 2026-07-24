from django.conf import settings
from django.contrib import admin
from apps.new_app.models import Project, Task, Tag, ProjectFile, Statuses, Priorities



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'count_files')
    search_fields = ('name',)

    @admin.action(description="замеет пробелы на подчеркивания")
    def space_to_underscore(self, request, queryset):
        for project in queryset:
            project.name = project.name.replace(' ', '_')
            project.save()
        return queryset
    actions = ['space_to_underscore']




@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'status', 'priority', 'created_at', 'due_date', 'assignee')
    list_filter = ('project', 'status', 'priority', 'created_at', 'due_date', 'assignee')
    search_fields =('name',)

    @admin.action(description="status closed")
    def tasks_close(self, request, queryset):
        for task in queryset:
            task.status = Statuses.CLOSED
            task.save()
        return queryset


    @admin.action(description="priority low")
    def task_low(self, request, queryset):
        for task in queryset:
            task.priority = Priorities.LOW
            task.save()
        return queryset

    @admin.action(description="priority low")
    def task_low(self, request, queryset):
        for task in queryset:
            task.priority = Priorities.LOW
            task.save()
        return queryset


    actions = ['task_low', "tasks_close"]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)


