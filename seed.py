import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.db.models.aggregates import Avg
from django.db.models.functions import ExtractWeekDay

import django
from django.core.management import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.new_app.models import ProjectFile, Project, Tag, Task, Statuses, Priorities
from django.utils import timezone
from django.db.models import Q, F, Count
import calendar
from django.contrib.auth.models import User
from django.core.paginator import Paginator

now = timezone.now()
_, last_day = calendar.monthrange(now.year, now.month)


# def task11():
#     filtered_project = Project.objects.filter(Q(created_at__lte=timezone.now()) & Q(name__icontains="TI"))
#     print(filtered_project)
#
# task11()
#
# def task11():
#     filtered_project = Project.objects.filter(created_at__lte=timezone.now(), name__icontains="TI")
#     print(filtered_project)
#
# task11()


# def task12():
#     all_files = ProjectFile.objects.filter(projects__name__icontains="SapHYR INC")
#     print(all_files)
#     # all_files = ProjectFile.objects.prefetch_related("projects").all()
#     # for f in all_files:
#     #     print(list(f.projects.values_list('name', flat=True)))
#
#
# task12()

# def task13():
#     all_task = Task.objects.filter(status=Statuses.NEW,priority=Priorities.URGENT)
#     print(all_task)
#
# task13()


# def task14():
#     task_to_update = Task.objects.filter(name="Update DB schema")
#     task_to_update.update(status="pending")
#
# task14()


# def task15():
#     tasks = Task.objects.filter(Q(status=Statuses.NEW) & Q(priority=Priorities.URGENT) | ~Q(tags__name="Design"))
#     for task in tasks:
#         print(task.status, task.priority, task.name)
#
#
#
# task15()

# def task16():
#     update_task = Task.objects.filter(due_date__gt=F("created_at__month")+1).update(priority=Priorities.CRITICAL)
# task16()

# def task17():
#     Task.objects.update(due_date=F('due_date') + timedelta(weeks=1))
# task17()

# def task18():
#     tasks = Task.objects.filter(assignee__isnull=True)
#     for task in tasks:
#         print(task.name)
#
#
# task18()
# def task19():
#     tasks = Task.objects.filter(tags__name__icontains="DevOPS")
#     for task in tasks:
#         print(task.name, task.status, task.priority, task.project)
#
# task19()

# def task20():
#     last_week = timezone.now() - timedelta(days=7)
#     files = ProjectFile.objects.filter(created_at__gte=last_week)
#     filtered_files = Project.objects.filter(files__in=files).distinct()
#     for file in filtered_files:
#         print(file.name, file.created_at)
# task20()

# def task21():
#     Task.objects.filter(status=Statuses.NEW).update(status=Statuses.IN_PROGRESS)
#
# task21()

# def task22():
#     three_days_more = F('due_date') + timedelta(days = 3)
#     tasks = Task.objects.filter(status=Statuses.IN_PROGRESS).update(due_date=three_days_more)#update(due_date=timezone.now()) добабляет дату в базу
# task22()

# def task23():
#     req_date_new = timezone.now().astimezone()
#     files = Project.objects.annotate(file_count=Count('files')).filter(Q(created_at__lt=req_date_new) & Q(file_count__gte=1))
#     print(files)
# task23()

def calculate_end_of_month():
    date_now = timezone.now()
    last_day = calendar.monthrange(date_now.year, date_now.month)[1]
    date = datetime(
        year= date_now.year,
        month=date_now.month,
        day=last_day,
    )
    return date.astimezone()

# def task24():
#     task_filtered = Task.objects.filter(Q(priority=Priorities.CRITICAL) | Q(priority=Priorities.URGENT),
#                                         due_date__lte=calculate_end_of_month())
#     print(task_filtered)
# task24()

# def task25():
#     tasks = Task.objects.exclude(Q(status=Statuses.PENDING) | Q(status=Statuses.CLOSED))
#     print(tasks)
# task25()

# def task26():
#     last_month = timezone.now() - relativedelta(month=1)
#     Task.objects.filter(project__name="TIGER", created_at__lte=last_month).update(priority=Priorities.URGENT)
# task26()

'''-------------Practic 30.07 -------------'''


# def task1():
#     cur_mont_projects = Project.objects.filter(created_at__month=timezone.now().month)
#     if cur_mont_projects:
#         for project in cur_mont_projects:
#             print(project.name, project.created_at)
#
#     else:
#         print("No projects in this month")
# task1()
#
# def task2():
#     monday = Project.objects.annotate(weekday=ExtractWeekDay('created_at')).filter(weekday=5)
#     if monday:
#         for project in monday:
#             print(project.name, project.created_at)
#     else:
#         print("No projects on Monday")
# task2()
#
# def task3():
#     task = Project.objects.all().count()
#     print(task)
# task3()

# def task4():
#     every_project = Project.objects.values('name','id').annotate(count=Count('files'))
#     for project in every_project:
#         print(project['name'], project['count'],project['id'])
#
# task4()
#
# def task5():
#     midle_task = Project.objects.annotate(task_count=Count('tasks')).aggregate(avg_count=Avg('s_count'))
#     print(midle_task)
# task5()

# def task6():
#     task_for_every_user = User.objects.annotate(task_count=Count('tasks'))
#     for user in task_for_every_user:
#         print(user.username,user.task_count)
# task6()

# def task7():
#     sort_task = Task.objects.order_by('priority','due_date')
#     for task in sort_task:
#         print(task.name, task.priority, task.due_date)
# task7()

# def task8():
#     project = User.objects.annotate(task_count=Count('tasks')).order_by('-task_count')
#     for user in project:
#         print(user.username,user.task_count)
# task8()

def task9():
    tasks = Task.objects.all()
    page = 2
    number_of_items = 10
    for task in tasks[(page-1)*number_of_items:page*number_of_items]:
        print(task)
task9()