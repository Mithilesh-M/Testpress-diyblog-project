from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

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
