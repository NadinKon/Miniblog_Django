from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text_comments')


# class CityForm(forms.ModelForm):
#     class Meta:
#         model = City
#         fields = ('name')