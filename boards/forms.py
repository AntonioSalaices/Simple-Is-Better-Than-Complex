from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': '¿Que estas pensando?'}
        ),
        max_length=4000,
        help_text='La longitud maxima por mensaje es de 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']