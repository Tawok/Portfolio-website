from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskCreationForm


# Create your views here.

class TaskListView(LoginRequiredMixin, ListView):
    template_name = "todos/task_list.html"
    model = Task
    context_object_name = 'tasks'
    ordering = ['complete']
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    tempalte_name = "todos/task_list.html"
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = "todos/create_task.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy('todos:task-list')

    def form_valid(self, form):
        obj_form = form.save(commit=False)
        obj_form.user = self.request.user
        obj_form.save()  
        return super().form_valid(form)

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    template_name = "todos/task_delete.html"
    model = Task
    success_url = reverse_lazy('todos:task-list')

class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = "todos/update_task.html"
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todos:task-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class TaskCompletedListView(LoginRequiredMixin, ListView):
    template_name = "todos/completed_list.html"
    model = Task
    context_object_name = 'tasks'
    ordering = ['complete']
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user, complete = True)

class TaskNonCompletedListView(LoginRequiredMixin, ListView):
    template_name = "todos/non_completed_list.html"
    model = Task
    context_object_name = 'tasks'
    ordering = ['complete']
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user, complete = False)
    



