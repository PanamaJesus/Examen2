from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from mi_app import models
from mi_app import forms

# Create your views here.
class CreateUser(generic.CreateView):
    template_name = "user/create_user.html"
    model = models.Usery
    form_class = forms.CreateUserForm
    success_url = reverse_lazy("users:list_user")


class ListUsers(generic.View):
    template_name = "user/list_user.html"
    context = {}

    def get(self, request):
        self.context = {
            "users" : models.Usery.objects.all()
            
        }
        return render(request, self.template_name,self.context)

class CreateTask(generic.CreateView):
    template_name = "task/create_task.html"
    model = models.Task
    form_class = forms.CreateTaskForm
    success_url = reverse_lazy("tasks:list_task")

class ListTasks(generic.View):
    template_name = "task/list_task.html"
    context = {}

    def get(self, request):
        self.context = {
            "tasks" : models.Task.objects.all(),
            "tasks_sinR": models.Task.objects.filter(status=False),
            "tasks_R": models.Task.objects.filter(status=True)


        }
        return render(request, self.template_name,self.context)
    
class UpdateTask(generic.UpdateView):
    template_name="task/update_task.html"
    model = models.Task
    form_class = forms.UpdateTaskForm
    success_url = reverse_lazy("tasks:list_task")

class DeleteTask(generic.DeleteView):
    template_name="task/delete_task.html"
    model = models.Task
    success_url = reverse_lazy("tasks:list_task")



