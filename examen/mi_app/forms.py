from django import forms
from mi_app import models

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = models.Usery
        fields = [
            "user_name"
        ]
        widgets = {}

# class UpdateUserForm(forms.models):
#     class Meta:
#         model= models.Usery
#         fields=[
#             "user_name"
#         ]
#         widgets= {}

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields=[
            "title",
            "description",
            "creator"
        ]
        widgets = {}

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model= models.Task
        fields=[
            "status"
        ]
        widgets= {}