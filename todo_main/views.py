from django.shortcuts import render
from todo.models import Task

def home(request):
   tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
   complete_tasks = Task.objects.filter(is_completed=True).order_by('updated_at')
   context = {
      'tasks' : tasks,
      'complete_tasks' : complete_tasks,
   }
   return render(request, 'home.html', context)