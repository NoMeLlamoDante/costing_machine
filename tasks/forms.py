from django import forms

from .models import Task


class TaskInitForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = ("task_name", "detalles")

        widgets = {
            "detalles": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "3",
                    "placeholder": "detalles del evento",
                }
            )
        }
