from django import forms

from .models import Topic, Actions

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class ActionForm(forms.ModelForm):
    class Meta:
        model = Actions
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
