from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author' ,'comment')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'what are you talking about'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'userid', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
            
        }

        

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'comment')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'what are you talking about'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control text-white'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
