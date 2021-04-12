from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Blog, Blogger, Comment

class CommentForm(forms.Form):
    description = forms.CharField(help_text="Enter comment about blog here.")

    def clean_description(self):
        data = self.cleaned_data['description']

        if len(data) == 0:
            raise ValidationError(_('Invalid description - description cannot be null'))

        if len(data) > 300:
            raise ValidationError(_('Invalid description - description should not be more than 300 characters'))

        if str(data).isspace():
            raise ValidationError(_('Invalid description - description cannot be blank'))

        return data

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=200, help_text="Enter the title of the Post")
    post_date = forms.DateField(help_text="Enter the date in this format MM/DD/YYYY")
    blogger = forms.ModelChoiceField(queryset=Blogger.objects.all(),help_text="Choose the Blogger")
    description = forms.CharField(max_length=500, help_text="Enter the description")

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        return data

class CreateBloggerForm(forms.Form):
    name = forms.CharField(max_length=200, help_text="Enter the name of blogger")
    bio = forms.CharField(max_length=500, help_text="Enter the bio of the Blogger")

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        return data
