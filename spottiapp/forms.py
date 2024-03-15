from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'comment')  # Include 'playlist' field in fields list

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'what are you talking about'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'comment')  # Include 'playlist' field in fields list

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'what are you talking about'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),

        }
