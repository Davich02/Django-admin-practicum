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

    @admin.action(description='Replace specific status to Done')
    def replace_status_to_done(self, request, tasks):
        tasks.update(status=Statuses.DONE)

    actions = [replace_status_to_done]

    priorities = [(priority.name, priority.value, priority.label) for priority in Priorities]
    for key, value, label in priorities:
        change_priority = lambda self, request, tasks, p=value: tasks.update(priority=p)
        change_priority.__name__ = key
        change_priority.short_description = f'Change specific priority to {label}'
        actions.append(change_priority)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)


