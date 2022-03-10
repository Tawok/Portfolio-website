from dataclasses import field
from tkinter import Widget
from turtle import width
from django import forms
from .models import Task

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','complete']
